# 🛡️ Raji: An Ancient Epic - AI Support Specialist

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://share.streamlit.io/)
[![Llama 3.3](https://img.shields.io/badge/LLM-Llama%203.3%20(Groq)-orange)](https://groq.com/)

A production-ready **Retrieval-Augmented Generation (RAG)** chatbot designed to act as a Tier-1 Technical Support Specialist for the game *Raji: An Ancient Epic*. This system bridges the gap between static documentation and interactive player assistance by providing real-time, verified troubleshooting.

---

## 🌟 Key Features

- **🔍 Context-Aware Troubleshooting:** Eliminates hallucinations by grounding LLM responses in a curated technical knowledge base.  
- **⚖️ Maximum Marginal Relevance (MMR):** Advanced retrieval logic that ensures the bot gathers diverse information (e.g., combining system specs + bug fixes) for a single query.  
- **⚡ Ultra-Low Latency:** Powered by Groq Cloud for near-instant inference and FAISS for millisecond vector lookups.  
- **💾 Local Persistence:** Automatically serializes the vector store to disk (`faiss_index`), preventing redundant compute on app restarts.  
- **📄 Exportable Support Guides:** One-click feature for players to download troubleshooting steps as local `.txt` files.  

---

## 🏗️ System Architecture

The pipeline follows a standard RAG pattern optimized for local deployment:

1. **Document Ingestion:** UTF-8 encoded text processing of `knowledge.txt`.  
2. **Semantic Chunking:** Recursive splitting (700 chars, 100 char overlap) to maintain context.  
3. **Vectorization:** Transformation of text into 384-dimensional vectors using `all-MiniLM-L6-v2`.  
4. **Retrieval & Synthesis:** MMR-based retrieval fed into a `ConversationalRetrievalChain` using **Llama 3.3-70B**.

---

## 📁 Project Structure

```text
Raji-game-support/
├── faiss_index/             # Local Vector Store (auto-generated)
│   ├── index.faiss          # Search index file
│   └── index.pkl            # Metadata file
├── .env                     # API Keys (Hidden)
├── .gitignore               # Files to ignore (e.g., .env, faiss_index/)
├── app.py                   # Main Streamlit application logic
├── knowledge.txt            # Raw text knowledge base
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

---

## 📋 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Raji-game-support.git
cd Raji-game-support
```

---

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_actual_api_key_here
```

*(Optional but recommended for monitoring)*

```
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=raji-support
```

---

### 4️⃣ Launch the Support Desk
```bash
streamlit run app.py
```

Your AI support assistant will now be running locally 🚀

---

## 🛑 Important Security Step — `.gitignore`

When uploading to GitHub, **never commit sensitive or auto-generated files**.

Create a `.gitignore` file and add:

```text
.env
faiss_index/
__pycache__/
.streamlit/
```

This protects your API keys and keeps the repository lightweight.

---

## 🎯 Ideal Use Cases

- AI-powered technical support  
- Game documentation assistants  
- Conversational RAG systems  
- Portfolio-ready GenAI projects  

---

## 👩‍💻 Author

**Prerna Prashar**  
📧 Email: prernaprashar7170@gmail.com
📞 Phone: +91-7070207015
🌐 GitHub: https://github.com/Prerna-Prahsar
🔗 LinkedIn: www.linkedin.com/in/prerna-parashar-15859728a



