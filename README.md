# Sentinel Tutor 🛡️📚

An AI-powered security-aware learning assistant that uses **Retrieval Augmented Generation (RAG)** to answer questions from user-provided study materials while also identifying cybersecurity risks like phishing.

---

## 🚨 Problem Statement
Students and learners often rely on scattered notes, PDFs, and online content to study.  
Traditional chatbots:
- Ignore personal study material
- Give generic answers
- Do not consider security threats in learning content

---

## 💡 Proposed Solution
Sentinel Tutor combines:
- **RAG (Retrieval Augmented Generation)** for personalized answers
- **Local LLM (Ollama – LLaMA 3)** for privacy
- **Security analysis module** to detect phishing or malicious intent

Users can ask questions and receive:
- Context-aware answers from their own notes
- Security-aware responses when content is risky

---

## ✨ Key Features
- PDF ingestion using sentence embeddings
- FAISS-based semantic search
- Local LLM inference using Ollama
- Phishing detection module
- FastAPI backend with interactive Swagger UI
- Privacy-first (no cloud LLM calls)

---

## 🏗️ Architecture Overview
User → FastAPI → RAG Engine → FAISS Index  
      ↘ Security Analyzer  
      ↘ Ollama (LLaMA 3)

---

## 🧰 Tech Stack
- Python
- FastAPI
- FAISS
- Sentence Transformers
- Ollama (LLaMA 3)
- PyPDF

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
python backend/rag/ingest.py
python -m uvicorn backend.main:app --reload

Open browser:
http://127.0.0.1:8000/docs
