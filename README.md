# 🛡️ Raji Support Bot — RAG-based Technical Support Assistant

An AI-powered support chatbot for the game **"Raji: An Ancient Epic"**, built with a Retrieval-Augmented Generation (RAG) pipeline. The bot answers player questions about bugs, crashes, performance issues, and gameplay blockers by retrieving relevant troubleshooting steps from a curated knowledge base and generating a grounded response — instead of relying on the LLM's raw, potentially hallucinated knowledge.

---

## 🚀 Key Features

- **Conversational RAG chatbot** — answers are grounded in a knowledge base of official troubleshooting docs, not just the LLM's parametric memory.
- **Semantic retrieval with FAISS** — knowledge base is chunked, embedded, and indexed for similarity search.
- **MMR retrieval** (Maximum Marginal Relevance) — balances relevance and diversity when pulling source chunks, reducing redundant context.
- **Conversation memory** — follow-up questions are understood in context of earlier turns in the chat.
- **Source transparency** — every answer shows the underlying knowledge-base excerpts it was generated from, so players (and reviewers) can verify the response isn't hallucinated.
- **Downloadable fix** — users can save the generated troubleshooting steps as a `.txt` file.
- **Persistent vector index** — FAISS index is built once and cached locally, so the app doesn't re-embed the knowledge base on every restart.
- **Custom support persona prompt** — the LLM is instructed to act as an official, professional support specialist with house rules (e.g. always mention "Restarting from Checkpoint" for gameplay bugs).

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| LLM | Groq API — Llama 3.3-70B-Versatile |
| Orchestration | LangChain (`langchain-classic` for memory/chains) |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` (sentence-transformers) |
| Vector Store | FAISS (local, persisted to disk) |
| Chunking | `RecursiveCharacterTextSplitter` (700 chars, 100 overlap) |
| Config | python-dotenv |

---

## 📐 How It Works

1. **Ingestion**: `knowledge.txt` (the official troubleshooting/FAQ doc) is loaded and split into ~700-character overlapping chunks.
2. **Embedding**: Each chunk is embedded using `all-MiniLM-L6-v2` and stored in a local FAISS index (cached to disk after first build, so subsequent runs skip re-embedding).
3. **Retrieval**: On each user query, the top relevant chunks are retrieved using **MMR** (k=4) to avoid returning near-duplicate chunks.
4. **Generation**: Retrieved chunks + chat history + the user's question are passed into a custom prompt template, and Llama 3.3-70B (via Groq) generates a support response.
5. **Memory**: `ConversationBufferMemory` keeps prior turns in context so the bot can handle follow-ups like "that didn't work, what else can I try?"

---

## 📂 Project Structure

```
raji-support-bot/
│
├── app_groq.py          # Main Streamlit application
├── knowledge.txt        # Source knowledge base (troubleshooting docs)
├── faiss_index/          # Persisted FAISS vector index (auto-generated on first run)
├── requirements.txt
├── .env                  # API keys (not committed)
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Prerna-Prahsar/raji-support-bot.git
cd raji-support-bot
```

### 2️⃣ Create environment
```bash
conda create -n raji-support python=3.10 -y
conda activate raji-support
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_api_key_here
```

### 5️⃣ Run the application
```bash
streamlit run app_groq.py
```
Then open your browser at:
```
http://localhost:8501
```

> Note: the first run will build and cache the FAISS index from `knowledge.txt`. Use the "🔄 Reload Support Data" button in the sidebar to force a rebuild if the knowledge base changes.

---

## 🧠 Skills Demonstrated

- Retrieval-Augmented Generation (RAG) pipeline design
- Semantic search & vector embeddings (FAISS, sentence-transformers)
- Prompt engineering (custom support-persona prompt template)
- LangChain orchestration (memory, conversational retrieval chains)
- LLM inference via Groq (Llama 3.3-70B)
- Streamlit application development & state management

---

## 👤 Author

**Prerna Prashar**
📧 prernaprashar7170@gmail.com
📞 +91-7070207015
🌐 GitHub: [Prerna-Prahsar](https://github.com/Prerna-Prahsar)
🔗 LinkedIn: [prerna-parashar](https://www.linkedin.com/in/prerna-parashar-15859728a)
