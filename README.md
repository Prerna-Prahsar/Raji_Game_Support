# 🎮 Raji AI Support Assistant

An intelligent AI-powered customer support system for the game **“Raji: An Ancient Epic”**.  
This project combines **LLM-based conversational AI, semantic search (RAG), automated ticketing, and an admin dashboard** into a single production-style application.

The system not only answers player questions but also automatically creates support tickets, suggests possible fixes, detects similar past issues, detects similar historical issues, and assigns confidence scoring — acting like a practical **AI Copilot for game support teams**.

---

## 🚀 Key Features

### 🧠 AI Chat Support
- Natural language chatbot powered by **Groq LLM / Gemini**.
- Uses **Retrieval-Augmented Generation (RAG)** with FAISS vector search for accurate answers.
- Maintains conversation memory for contextual responses.

### 🎫 Smart Ticketing System
- Automatically creates tickets when issues are detected.
- Intelligent classification:
  - Category (bug, performance, gameplay, account, general)
  - Priority (low / medium / high)
  - Device information extraction (GPU, RAM, laptop, OS).
- Persistent CSV-based storage.

### 🤖 Auto-Resolution Suggestions (AI Copilot)
- Generates suggested fixes using LLM reasoning.
- Finds similar historical tickets using embeddings similarity.
- Assigns confidence score to each solution.

### 📊 Admin Dashboard
- View all tickets in real-time.
- Filter by category, priority, and status.
- Export filtered tickets as CSV.
- Confidence highlighting for faster triage.

### 📱 UX & UI Enhancements
- Mobile-friendly responsive layout.
- Auto-scroll chat interface.
- Ask button for submitting questions.
- Loading indicators while AI is processing.
- Clean operational dashboard.

---

## 🧠 Skills & Technical Expertise Demonstrated

### 🔹 Artificial Intelligence & Machine Learning
- Natural Language Processing (NLP)
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Embeddings & Vector Search
- Semantic Similarity Matching
- Model Integration (Groq, Gemini)

### 🔹 Software Engineering
- Python Application Development
- Modular Code Architecture
- API Integration
- Error Handling & Logging
- Environment Management (conda, venv)

### 🔹 Data Engineering & Analytics
- FAISS Vector Indexing
- CSV-based Data Pipelines
- Pandas Data Analysis
- Ticket Analytics & Filtering

### 🔹 Web & UI Development
- Gradio UI Development
- Responsive UI Design
- UX Optimization
- Dashboard Interfaces

### 🔹 DevOps & Tooling
- Git & GitHub
- Environment Variables (.env)
- Dependency Management
- Project Structuring
- Deployment Readiness

---

## 🏗️ Tech Stack

- **Python 3.10+**
- **Gradio** – Web UI
- **LangChain** – LLM Orchestration
- **Groq API / Gemini API** – Language Models
- **FAISS** – Vector Similarity Search
- **HuggingFace Sentence Transformers** – Embeddings
- **Pandas** – Ticket Analytics
- **dotenv** – Environment Variable Management

---

## 📂 Project Structure
raji_customer_service/
│
├── app_groq.py
├── app_gemini.py
├── tickets/
│ └── tickets.csv
├── faiss_index/
├── .env
├── .gitignore
└── README.md

### 1️⃣ Clone the repository
```bash
git clone https://github.com/NishantNirmalSingh/raji_customer_service.git
cd raji_customer_service

2️⃣ Create environment
conda create -n venv python=3.10 -y
conda activate venv

conda create -n groqenv python=3.11 -y
conda activate groqenv

3️⃣ Install dependencies
pip install -r requirements.txt


4️⃣ Setup Environment Variables

Create a .env file in project root:
GOOGLE_API_KEY=your_api_key_here
GROQ_API_KEY=your_api_key_here

5️⃣ Run the application
python app_groq.py  change python kernal press ctrl+shift+P and choose groqenv 3.11
python app_gemini.py  change python kernal press ctrl+shift+P and choose venv 3.10
Open browser:
http://127.0.0.1:7860


👤 Authors

Prerna Prashar
📧 Email: prernaprashar7170@gmail.com
📞 Phone: +91-7070207015
🌐 GitHub: https://github.com/Prerna-Prahsar
🔗 LinkedIn: www.linkedin.com/in/prerna-parashar-15859728a

