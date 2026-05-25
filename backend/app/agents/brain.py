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
        """
        combined_text = " ".join(context_chunks)
        topic_hash = hashlib.md5(combined_text[:1000].encode()).hexdigest()

        # In a real system, this would be a summarization/synthesis step
        synthesis = f"Synthesizing knowledge from {len(context_chunks)} sacred fragments..."
        self.memory_cache[topic_hash] = synthesis
        return synthesis

    async def consult_brain(self, query: str):
        # 1. Retrieve raw context (the 'eternal memory')
        raw_context = retrieval_service.retrieve_context(query, limit=5)

        # 2. Learn/Synthesize the specific context for this query
        synthesis_note = await self.learn_from_context(raw_context)

        # 3. Consult the Knowledge Graph for deeper relations
        relations = await knowledge_graph.get_relations(query)

        # 4. Final 'Thought' synthesis
        # Combining RAG, KG, and Persona-specific synthesis
        thought = {
            "query": query,
            "synthesis": synthesis_note,
            "wisdom_nugget": raw_context[0] if raw_context else "The silence of the ages.",
            "connections": relations,
            "certainty": 0.85 if raw_context else 0.1
        }

        return thought

brain_agent = BrainAgent()
