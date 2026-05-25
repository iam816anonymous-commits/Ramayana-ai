import sys
import os
from sentence_transformers import SentenceTransformer

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app.services.vector_db import vector_db

def ingest():
    # Initialize model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    vector_size = model.get_sentence_embedding_dimension()

    # Ensure collection exists (using persistent storage for this script)
    # Note: In-memory Qdrant won't persist across processes unless we use a file or server.
    # For simplicity in this demo, let's use a local path if we want persistence,
    # but since I'll run the server in the same environment, I might need a server or local file.
    vector_db.client = vector_db.client.__class__(path="qdrant_storage")
    vector_db.ensure_collection(vector_size)

    # Read data
    with open('data/sample_ramayana.txt', 'r') as f:
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
