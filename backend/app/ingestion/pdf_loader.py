import os
from PyPDF2 import PdfReader

class PDFLoader:
    def load(self, filepath: str):
        reader = PdfReader(filepath)
        documents = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                documents.append({
                    "text": text,
                    "metadata": {
                        "source": filepath,
                        "page": i + 1,
                        "type": "pdf_document",
                        "filename": os.path.basename(filepath)
                    }
                })
        return documents
