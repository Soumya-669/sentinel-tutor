# Sentinel Tutor 🛡️🤖

Sentinel Tutor is a secure AI-powered learning assistant designed to answer questions from user-provided notes while protecting against phishing, unsafe prompts, and malicious content.

---

## 🚀 Features
- Retrieval-Augmented Generation (RAG)
- PDF-based knowledge ingestion
- Semantic search using FAISS
- Local LLM inference with Ollama
- Phishing & unsafe prompt detection
- FastAPI backend with Swagger UI

---

## 🏗️ Architecture
User → FastAPI → Security Filter → RAG Retriever → LLM (Ollama) → Secure Response

---

## 🛠️ Tech Stack
- Python
- FastAPI
- FAISS
- Sentence Transformers
- Ollama (LLaMA3)
- PyPDF

---

## 📂 Project Structure

backend/
├── main.py
├── rag/
├── security/
└── data/

## ▶️ How to Run
```bash
python backend/rag/ingest.py
python -m uvicorn backend.main:app --reload
