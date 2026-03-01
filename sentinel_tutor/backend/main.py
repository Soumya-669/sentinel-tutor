from fastapi import FastAPI
from backend.rag.query import ask_question
from backend.security.phishing import check_text

app = FastAPI()

@app.post("/ask")
def ask(payload: dict):
    question = payload["question"]

    # 🔐 Step 1: security check
    security_result = check_text(question)

    if security_result["is_phishing"]:
     return {
        "warning": "⚠️ Potential phishing detected",
        "risk_level": security_result["risk_level"],
        "reason": security_result["matched_patterns"]
    }

    # 🤖 Step 2: normal RAG flow
    answer = ask_question(question)
    return {"answer": answer}