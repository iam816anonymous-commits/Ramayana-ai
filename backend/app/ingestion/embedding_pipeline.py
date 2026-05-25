import hashlib
from sentence_transformers import SentenceTransformer
from backend.app.core.vector_store import vector_db
from backend.app.models.metadata import metadata_store

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

        for i, (doc, emb) in enumerate(zip(processed_docs, embeddings)):
            # Use deterministic ID based on content hash to avoid duplication
            content_hash = hashlib.md5(doc['text'].encode()).hexdigest()
            point_id = content_hash

            ids.append(point_id)
            payloads.append({
                "text": doc['text'],
                **doc['metadata']
            })
            metadata_store.store_document_metadata(point_id, doc['metadata'])

        vector_db.upsert_vectors(ids, embeddings, payloads)
        print(f"Stored {len(processed_docs)} chunks in Qdrant.")
