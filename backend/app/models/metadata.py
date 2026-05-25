# Placeholder for Postgres metadata storage
# In V4, we will implement actual SQLAlchemy models here.

class MetadataStore:
    def __init__(self):
        pass

    def store_document_metadata(self, doc_id: str, metadata: dict):
        # Future: Insert into Postgres
        pass

metadata_store = MetadataStore()
