import os
from sentence_transformers import SentenceTransformer
from backend.app.core.vector_store import vector_db

class RetrievalService:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def retrieve_context(self, query: str, limit: int = 2):
        query_vector = self.model.encode(query).tolist()
        results = vector_db.search(query_vector, limit=limit)
        return [res.payload['text'] for res in results]

retrieval_service = RetrievalService()
