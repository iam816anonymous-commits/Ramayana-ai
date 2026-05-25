from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

class VectorDBService:
    def __init__(self, location=":memory:"):
        self.client = QdrantClient(location=location)
        self.collection_name = "ramayana_docs"

    def ensure_collection(self, vector_size: int):
        collections = self.client.get_collections().collections
        exists = any(c.name == self.collection_name for c in collections)
        if not exists:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
            )

    def upsert_vectors(self, ids, vectors, payloads):
        from qdrant_client.http.models import PointStruct
        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                PointStruct(id=idx, vector=vec, payload=payload)
                for idx, vec, payload in zip(ids, vectors, payloads)
            ],
        )

    def search(self, vector, limit=3):
        return self.client.query_points(
            collection_name=self.collection_name,
            query=vector,
            limit=limit,
        ).points

vector_db = VectorDBService()
