import os
import glob
from backend.app.ingestion.json_loader import JSONLoader
from backend.app.ingestion.txt_loader import TXTLoader
from backend.app.ingestion.pdf_loader import PDFLoader
from backend.app.ingestion.cleaner import Cleaner
from backend.app.ingestion.chunker import Chunker
from backend.app.ingestion.embedding_pipeline import EmbeddingPipeline

class IngestionPipeline:
    def __init__(self):
        self.json_loader = JSONLoader()
        self.txt_loader = TXTLoader()
        self.pdf_loader = PDFLoader()
        self.cleaner = Cleaner()
        self.chunker = Chunker()
        self.embedding_pipeline = EmbeddingPipeline()

    def scan_data_folder(self, root_dir="data"):
        all_processed_docs = []

        # JSON
        for filepath in glob.glob(os.path.join(root_dir, "json", "*.json")):
            print(f"Loading JSON: {filepath}")
            docs = self.json_loader.load(filepath)
            all_processed_docs.extend(self._process_docs(docs))

        # TXT
        for filepath in glob.glob(os.path.join(root_dir, "txt", "**", "*.txt"), recursive=True):
            print(f"Loading TXT: {filepath}")
            docs = self.txt_loader.load(filepath)
            all_processed_docs.extend(self._process_docs(docs))

        # PDF
        for filepath in glob.glob(os.path.join(root_dir, "pdf", "*.pdf")):
            print(f"Loading PDF: {filepath}")
            docs = self.pdf_loader.load(filepath)
            all_processed_docs.extend(self._process_docs(docs))

        # Embed and Store
        if all_processed_docs:
            self.embedding_pipeline.process_and_store(all_processed_docs)
            print(f"Ingestion complete. Total chunks: {len(all_processed_docs)}")
        else:
            print("No new data found for ingestion.")

    def _process_docs(self, docs):
        processed = []
        for doc in docs:
            cleaned_text = self.cleaner.clean(doc['text'])
            chunks = self.chunker.chunk(cleaned_text)
            for chunk in chunks:
                processed.append({
                    "text": chunk,
                    "metadata": doc['metadata']
                })
        return processed

ingestion_pipeline = IngestionPipeline()
