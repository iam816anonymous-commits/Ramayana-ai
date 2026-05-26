from typing import List, Dict, Any

class ContextMerger:
    """
    Merges multiple retrieved fragments into a coherent context block for LLM processing.
    Handles deduplication and ranking-based formatting.
    """
    def merge(self, fragments: List[Dict[str, Any]]) -> str:
        if not fragments:
            return ""

        # Sort by score if available
        sorted_fragments = sorted(fragments, key=lambda x: x.get('score', 0), reverse=True)

        merged = "SCRED FRAGMENTS:\n\n"
        for i, frag in enumerate(sorted_fragments):
            content = frag.get('content', str(frag))
            source = frag.get('metadata', {}).get('source', 'Unknown Source')
            merged += f"Fragment {i+1} [Source: {source}]:\n{content}\n\n"

        return merged

context_merger = ContextMerger()
