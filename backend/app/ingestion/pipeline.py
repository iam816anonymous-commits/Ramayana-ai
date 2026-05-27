import os
import glob
from app.ingestion.json_loader import JSONLoader
from app.ingestion.valmiki_loader import valmiki_loader
from app.ingestion.txt_loader import TXTLoader
from app.ingestion.pdf_loader import PDFLoader
from app.ingestion.csv_loader import CSVLoader
from app.ingestion.cleaner import Cleaner
from app.ingestion.semantic_processor import SemanticChunker, EventExtractor
from app.ingestion.shloka_processor import ShlokaProcessor
from app.ingestion.metadata_mapper import MetadataMapper
from app.ingestion.embedding_pipeline import EmbeddingPipeline
from app.ingestion.mythology_index import myth_index
from app.core.vector_store import vector_db

class IngestionPipeline:
    def __init__(self):
        self.json_loader = JSONLoader()
        self.txt_loader = TXTLoader()
        self.pdf_loader = PDFLoader()
        self.csv_loader = CSVLoader()
        self.cleaner = Cleaner()
        self.chunker = SemanticChunker(max_chars=1200, min_chars=200)
        self.shloka_proc = ShlokaProcessor()
        self.mapper = MetadataMapper()
        self.extractor = EventExtractor()
        self.embedding_pipeline = EmbeddingPipeline()

    def reset_collection(self):
        """Clears the collection for a fresh re-ingestion."""
        print(f"Resetting collection: {vector_db.collection_name}")
        try:
            vector_db.client.delete_collection(collection_name=vector_db.collection_name)
        except Exception as e:
            print(f"Note: Could not delete collection: {e}")

    def scan_data_folder(self, root_dir="data", reset=False):
        if reset:
            self.reset_collection()

        all_processed_docs = []

        # 1. JSON
        for filepath in glob.glob(os.path.join(root_dir, "json", "*.json")):
            if "Valmiki_Ramayan_Shlokas.json" in filepath:
                print(f"Loading specialized Valmiki JSON: {filepath}")
                docs = valmiki_loader.load(filepath)
                all_processed_docs.extend(self._process_shloka_docs(docs, is_direct=True))
            else:
                print(f"Loading JSON: {filepath}")
                docs = self.json_loader.load(filepath)
                all_processed_docs.extend(self._process_generic_docs(docs))

        # 2. TXT
        for filepath in glob.glob(os.path.join(root_dir, "txt", "**", "*.txt"), recursive=True):
            print(f"Loading TXT: {filepath}")
            docs = self.txt_loader.load(filepath)
            all_processed_docs.extend(self._process_generic_docs(docs))

        # 3. CSV (Shlokas)
        os.makedirs(os.path.join(root_dir, "csv"), exist_ok=True)
        for filepath in glob.glob(os.path.join(root_dir, "csv", "*.csv")):
            print(f"Loading CSV: {filepath}")
            shlokas = self.csv_loader.load(filepath)
            all_processed_docs.extend(self._process_shloka_docs(shlokas))

        # Build Mythology Index
        myth_index.build_from_payloads(all_processed_docs)
        myth_index.save()
        print(f"Mythology indices updated.")

        # Embed and Store
        if all_processed_docs:
            print(f"Processing {len(all_processed_docs)} chunks...")
            self.embedding_pipeline.process_and_store(all_processed_docs)
            print(f"Ingestion complete. Total chunks stored: {len(all_processed_docs)}")
        else:
            print("No new data found for ingestion.")

    def _process_generic_docs(self, docs):
        processed = []
        for doc in docs:
            cleaned_text = self.cleaner.clean(doc['text'])
            chunks = self.chunker.chunk(cleaned_text)
            for chunk in chunks:
                entities = self.extractor.extract(chunk)
                metadata = {**doc['metadata'], **entities}
                processed.append({"text": chunk, "metadata": metadata})
        return processed

    def _process_shloka_docs(self, shlokas, is_direct=False):
        # Shlokas are treated as individual units, no semantic chunking across them
        if not is_direct:
            shlokas = self.shloka_proc.process(shlokas)

        processed = []
        for s in shlokas:
            entities = self.extractor.extract(s['text'])
            s['metadata'].update(entities)
            enriched = self.mapper.enrich(s)
            processed.append(enriched)
        return processed

ingestion_pipeline = IngestionPipeline()
