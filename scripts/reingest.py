import os
import sys
from unittest.mock import MagicMock

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), "backend"))

from app.ingestion.pipeline import IngestionPipeline

def test_reingestion():
    pipeline = IngestionPipeline()
    print("Starting re-ingestion with Semantic Chunker...")
    # Using reset=True to ensure we don't have duplicates and only new semantic chunks
    pipeline.scan_data_folder(reset=True)
    print("Re-ingestion successful.")

if __name__ == "__main__":
    test_reingestion()
