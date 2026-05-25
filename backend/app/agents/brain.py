from backend.app.core.retrieval import retrieval_service
from backend.app.core.knowledge_graph import knowledge_graph
import hashlib

class BrainAgent:
    """
    The Brain Agent acts as the central intelligence of the Ramayana AI.
    It "learns" by processing retrieved context and maintaining a synthesized
    view of the mythology.
    """
    def __init__(self):
        self.memory_cache = {} # Synthetic memory of processed topics

    async def learn_from_context(self, context_chunks: list):
        """
        Simulates the process of 'learning' or synthesizing a topic.
        The Brain Agent identifies patterns and thematic resonance across fragments.
        """
        if not context_chunks:
            return "Seeking clarity in the void..."

        combined_text = " ".join(context_chunks)
        topic_hash = hashlib.md5(combined_text[:1000].encode()).hexdigest()

        # Enhanced synthesis logic: identifying themes
        themes = []
        if any(word in combined_text.lower() for word in ["dharma", "duty", "right"]):
            themes.append("Dharma (Eternal Law)")
        if any(word in combined_text.lower() for word in ["bhakti", "devotion", "love"]):
            themes.append("Bhakti (Devotion)")
        if any(word in combined_text.lower() for word in ["war", "battle", "astra"]):
            themes.append("Shastra (Martial Wisdom)")
        if any(word in combined_text.lower() for word in ["forest", "exile", "vanavasa"]):
            themes.append("Aranya (Wilderness Reflection)")

        theme_str = f" interwoven with themes of {', '.join(themes)}" if themes else ""
        synthesis = f"Synthesizing {len(context_chunks)} sacred fragments{theme_str} into a singular vision..."

        self.memory_cache[topic_hash] = synthesis
        return synthesis

    async def consult_brain(self, query: str):
        """
        Coordinates the retrieval and synthesis process.
        """
        # 1. Retrieve raw context (the 'eternal memory')
        raw_context = retrieval_service.retrieve_context(query, limit=5)

        # 2. Learn/Synthesize the specific context for this query
        synthesis_note = await self.learn_from_context(raw_context)

        # 3. Consult the Knowledge Graph for deeper relations
        relations = await knowledge_graph.get_relations(query)

        # 4. Final 'Thought' synthesis
        # Combining RAG, KG, and thematic synthesis
        thought = {
            "query": query,
            "synthesis": synthesis_note,
            "wisdom_nugget": raw_context[0] if raw_context else "Even in silence, there is a lesson to be found.",
            "all_fragments": raw_context,
            "connections": relations,
            "certainty": 0.85 if raw_context else 0.1
        }

        return thought

brain_agent = BrainAgent()
