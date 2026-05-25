import sys
import os
from sentence_transformers import SentenceTransformer

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.vector_store import vector_db

def ingest():
    # Initialize model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    vector_size = model.get_embedding_dimension()

    # Use persistent storage
    vector_db.client = vector_db.client.__class__(path="qdrant_storage")
    vector_db.ensure_collection(vector_size)

    # Read data
    with open('data/txt/sample_ramayana.txt', 'r') as f:
        text = f.read()

    # Simple chunking by paragraph
    chunks = [c.strip() for c in text.split('\n\n') if c.strip()]

    # Generate embeddings
    embeddings = model.encode(chunks).tolist()

    # Upsert
    ids = list(range(len(chunks)))
    payloads = [{"text": chunk} for chunk in chunks]

    vector_db.upsert_vectors(ids, embeddings, payloads)
    print(f"Ingested {len(chunks)} chunks into Qdrant.")

if __name__ == "__main__":
    ingest()
