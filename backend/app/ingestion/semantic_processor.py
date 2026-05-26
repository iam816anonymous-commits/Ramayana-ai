import nltk
from nltk.tokenize import sent_tokenize
from typing import List, Dict, Any
import os

# Download necessary NLTK data
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

class SemanticChunker:
    """
    Groups sentences based on semantic coherence and metadata boundaries.
    """
    def __init__(self, max_chars: int = 1500, min_chars: int = 300, overlap_sentences: int = 1):
        self.max_chars = max_chars
        self.min_chars = min_chars
        self.overlap_sentences = overlap_sentences

    def chunk(self, text: str) -> List[str]:
        # Step 1: Split into sentences
        sentences = sent_tokenize(text)

        chunks = []
        current_chunk = []
        current_length = 0

        for i, sentence in enumerate(sentences):
            sent_len = len(sentence)

            # If adding this sentence exceeds max_chars, finalize current chunk
            if current_length + sent_len > self.max_chars and current_chunk:
                chunks.append(" ".join(current_chunk))

                # Handle overlap: keep last N sentences for context
                overlap = current_chunk[-self.overlap_sentences:] if self.overlap_sentences > 0 else []
                current_chunk = overlap + [sentence]
                current_length = sum(len(s) for s in current_chunk) + len(current_chunk) - 1
            else:
                current_chunk.append(sentence)
                current_length += sent_len + (1 if current_length > 0 else 0)

        # Add the last chunk if it meets min requirements or is the only one
        if current_chunk:
            final_str = " ".join(current_chunk)
            if len(final_str) >= self.min_chars or not chunks:
                chunks.append(final_str)
            elif chunks:
                # Merge small tail into previous chunk if possible
                if len(chunks[-1]) + len(final_str) < self.max_chars:
                    chunks[-1] = chunks[-1] + " " + final_str
                else:
                    chunks.append(final_str)

        return chunks

class EventExtractor:
    """
    Extracts entities and events to enrich chunk metadata.
    """
    def __init__(self):
        # In a real production system, this would use a small NER model or LLM.
        # For Phase 1.5, we use a high-recall keyword matcher for key Ramayana entities.
        self.key_entities = {
            "characters": ["Rama", "Sita", "Hanuman", "Lakshmana", "Ravana", "Dasharatha", "Kaikeyi", "Sugriva", "Valmiki", "Tulsidas"],
            "locations": ["Ayodhya", "Lanka", "Dandaka", "Panchavati", "Kishkindha", "Mithila", "Chitrakoot"],
            "concepts": ["Dharma", "Karma", "Bhakti", "Tyaga", "Moksha", "Artha"]
        }

    def extract(self, text: str) -> Dict[str, List[str]]:
        found = {
            "characters": [],
            "locations": [],
            "concepts": []
        }

        lower_text = text.lower()
        for category, keywords in self.key_entities.items():
            for kw in keywords:
                if kw.lower() in lower_text:
                    found[category].append(kw)

        return found
