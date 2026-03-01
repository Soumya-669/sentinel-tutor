import faiss, pickle
from sentence_transformers import SentenceTransformer
from .ollama_client import ask_llama

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("backend/data/index.faiss")

with open("backend/data/chunks.pkl", "rb") as f:
    texts, sources = pickle.load(f)

def ask_question(question):
    q_emb = model.encode([question])
    D, I = index.search(q_emb, k=3)

    context = "\n".join([texts[i] for i in I[0]])

    prompt = f"""
Answer using ONLY the context below:

{context}

Question: {question}
"""

    return ask_llama(prompt)