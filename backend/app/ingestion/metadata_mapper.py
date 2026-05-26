from typing import Dict, Any, List

class MetadataMapper:
    """
    Enriches shloka metadata with calculated fields or taxonomic tags.
    """
    def enrich(self, doc: Dict[str, Any]) -> Dict[str, Any]:
        meta = doc['metadata']

        # Determine specific mythological importance based on keywords
        text = doc['text'].lower()

        # Basic character tagging (redundant with EventExtractor but more specific to verse structure)
        tags = []
        if "rama" in text: tags.append("Rama")
        if "sita" in text: tags.append("Sita")
        if "hanuman" in text: tags.append("Hanuman")

        meta['characters'] = list(set(meta.get('characters', []) + tags))

        return doc
