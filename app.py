import streamlit as st
import os
from dotenv import load_dotenv

# LangChain & AI Imports
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# CLASSIC COMPONENTS
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.prompts import PromptTemplate

# 1. SETUP & CONFIG
load_dotenv()
st.set_page_config(page_title="Raji Support Bot", page_icon="🛡️", layout="wide")

# Sidebar for controls
with st.sidebar:
    st.title("🛡️ Support Desk")
    
    # Status Indicator
    if os.path.exists("faiss_index"):
        st.success("✅ Knowledge Base: Ready")
    else:
        st.warning("⚠️ Knowledge Base: Needs Loading")

    if st.button("🗑️ Reset Support Session"):
        st.session_state.chat_history = []
        if "chain" in st.session_state:
            st.session_state.chain.memory.clear()
        st.rerun()
    
    if st.button("🔄 Reload Support Data"):
        if os.path.exists("faiss_index"):
            import shutil
            shutil.rmtree("faiss_index")
        st.cache_resource.clear()
        st.rerun()
    
    st.markdown("---")
    st.info("This bot provides official troubleshooting for Raji: An Ancient Epic.")

st.title("🛡️ Raji: An Ancient Epic Support")
st.caption("Solving technical issues and gameplay hurdles in real-time.")

# 2. THE BRAIN: VECTOR DB
@st.cache_resource
def get_vector_store():
    index_path = "faiss_index"
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    if os.path.exists(index_path):
        return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    
    if not os.path.exists("knowledge.txt"):
        st.error("Missing knowledge.txt file!")
        return None
    
    try:
        loader = TextLoader("knowledge.txt", encoding="utf-8")
        docs = loader.load()
    except Exception as e:
        st.error(f"Error reading knowledge.txt: {e}")
        return None

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)
    final_docs = text_splitter.split_documents(docs)
    
    vectorstore = FAISS.from_documents(final_docs, embeddings)
    vectorstore.save_local(index_path)
    return vectorstore

# 3. SUPPORT PROMPT
custom_template = """
You are the Technical Support Specialist for 'Raji: An Ancient Epic'. 
Help the player solve their problem using the context provided.

RULES:
1. Be professional and supportive.
2. Provide numbered troubleshooting steps.
3. If you can't find a specific fix, suggest restarting the game or checking drivers.
4. Always mention 'Restarting from Checkpoint' for gameplay bugs.

Context: {context}
Chat History: {chat_history}
Question: {question}
Support Response:"""

CUSTOM_PROMPT = PromptTemplate(template=custom_template, input_variables=["context", "chat_history", "question"])

# 4. INITIALIZE
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = get_vector_store()

if "chain" not in st.session_state and st.session_state.vector_store:
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.3, streaming=True)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key="answer")
    
    st.session_state.chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=st.session_state.vector_store.as_retriever(search_type="mmr", search_kwargs={'k': 4}),
        memory=memory,
        combine_docs_chain_kwargs={"prompt": CUSTOM_PROMPT},
        return_source_documents=True
    )

# 5. UI: CHAT
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Describe your issue (e.g., 'Game keeps crashing' or 'Stuck in a level')..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.session_state.chain.invoke({"question": prompt})
        full_response = response["answer"]
        
        # Display response
        st.write(full_response) 
        
        # --- NEW FEATURES ---
        col1, col2 = st.columns([1, 4])
        with col1:
            # Download Button for the Fix
            st.download_button(
                label="💾 Save Fix",
                data=full_response,
                file_name="Raji_Troubleshooting_Guide.txt",
                mime="text/plain",
                help="Download this solution to follow it while the game is closed."
            )
        
        with st.expander("📚 View Technical References"):
            for doc in response["source_documents"]:
                st.caption(f"- {doc.page_content[:250]}...")

    st.session_state.chat_history.append({"role": "assistant", "content": full_response})