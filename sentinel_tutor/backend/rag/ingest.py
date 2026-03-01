from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss, os, pickle

PDF_DIR = "notes"
DATA_DIR = "backend/data"
os.makedirs(DATA_DIR, exist_ok=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = []
sources = []

for file in os.listdir(PDF_DIR):
    if file.endswith(".pdf"):
        reader = PdfReader(os.path.join(PDF_DIR, file))
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                texts.append(text)
                sources.append(f"{file} page {i+1}")

embeddings = model.encode(texts)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, f"{DATA_DIR}/index.faiss")

with open(f"{DATA_DIR}/chunks.pkl", "wb") as f:
    pickle.dump((texts, sources), f)

print("✅ PDF ingestion complete")