import os
from sentence_transformers import SentenceTransformer
from app.core.vector_store import vector_db

class RetrievalService:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def retrieve_context(self, query: str, limit: int = 5):
        query_vector = self.model.encode(query).tolist()
        results = vector_db.search(query_vector, limit=limit)

        # Return enriched objects with metadata for citations and shloka structure
        processed_results = []
        for res in results:
            meta = res.payload.get('metadata', {})

            item = {
                "content": res.payload['text'],
                "score": res.score,
                "metadata": meta,
                "type": meta.get("type", "document")
            }

            # Specific handling for shlokas to help the frontend/agent
            if item["type"] == "shloka":
                item["shloka"] = meta.get("shloka_raw")
                item["translation"] = meta.get("translation_raw")
                item["verse_ref"] = meta.get("verse_ref")
                item["book"] = meta.get("book")

            processed_results.append(item)

        return processed_results

retrieval_service = RetrievalService()
