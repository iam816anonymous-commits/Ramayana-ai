import hashlib
import uuid
from sentence_transformers import SentenceTransformer
from app.core.vector_store import vector_db
from app.models.metadata import metadata_store

class EmbeddingPipeline:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def process_and_store(self, processed_docs):
        # processed_docs: list of {text, metadata}
        if not processed_docs:
            return

        texts = [doc['text'] for doc in processed_docs]
        embeddings = self.model.encode(texts).tolist()

        vector_size = self.model.get_embedding_dimension()
        vector_db.ensure_collection(vector_size)

        ids = []
        payloads = []

        # Namespace for deterministic UUIDs
        namespace = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8') # DNS Namespace as base

        for i, (doc, emb) in enumerate(zip(processed_docs, embeddings)):
            # Use deterministic UUID based on content hash to avoid duplication
            # and ensure strict UUID format compatibility.
            content_hash = hashlib.md5(doc['text'].encode()).hexdigest()
            point_id = str(uuid.uuid5(namespace, content_hash))

            ids.append(point_id)
            payloads.append({
                "text": doc['text'],
                "metadata": doc['metadata']
            })
            metadata_store.store_document_metadata(point_id, doc['metadata'])

        vector_db.upsert_vectors(ids, embeddings, payloads)
        print(f"Stored {len(processed_docs)} chunks in Qdrant.")
