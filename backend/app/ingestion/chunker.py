import re

class Chunker:
    def __init__(self, chunk_size=500, chunk_overlap=50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self, text: str):
        # Paragraph-based chunking
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]

        final_chunks = []
        for p in paragraphs:
            if len(p) <= self.chunk_size:
                final_chunks.append(p)
            else:
                # Fallback to fixed size for large paragraphs
                start = 0
                while start < len(p):
                    end = start + self.chunk_size
                    final_chunks.append(p[start:end])
                    start += self.chunk_size - self.chunk_overlap

        return final_chunks
