from typing import List, Dict, Any

class ShlokaProcessor:
    """
    Handles granular processing of shlokas to ensure they are high-quality retrieval units.
    """
    def process(self, shlokas: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        processed = []
        for shloka in shlokas:
            # Metadata normalization
            meta = shloka['metadata']

            # Map kanda names to full book titles if needed
            kanda_map = {
                "Bala": "Bala Kanda",
                "Ayodhya": "Ayodhya Kanda",
                "Aranya": "Aranya Kanda",
                "Kishkindha": "Kishkindha Kanda",
                "Sundara": "Sundara Kanda",
                "Yuddha": "Yuddha Kanda",
                "Uttara": "Uttara Kanda"
            }

            meta['book'] = kanda_map.get(meta['kanda'], meta['kanda'])
            meta['verse_ref'] = meta['verse']

            processed.append(shloka)
        return processed
