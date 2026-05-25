from backend.app.core.retrieval import retrieval_service
from backend.app.core.knowledge_graph import knowledge_graph
from backend.app.agents.seeker import seeker_agent
from backend.app.services.brain_store import brain_store
import hashlib

class BrainAgent:
    """
    The Brain Agent acts as the central intelligence of the Ramayana AI.
    It "learns" by processing retrieved context and maintaining a synthesized
    view of the mythology.
    """
    def __init__(self):
        self.memory_cache = {} # Synthetic memory of processed topics

    async def learn_from_context(self, context_chunks: list, query: str = ""):
        """
        Simulates the process of 'learning' or synthesizing a topic.
        The Brain Agent identifies patterns and thematic resonance across fragments,
        then engages in a dialogue with the Seeker Agent to refine the wisdom.
        """
        if not context_chunks:
            return "Seeking clarity in the void..."

        combined_text = " ".join(context_chunks)

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
        base_synthesis = f"Synthesizing {len(context_chunks)} sacred fragments{theme_str} into a singular vision..."

        # Dialectical Refinement: Brain asks Seeker to challenge this synthesis
        challenge = await seeker_agent.pose_challenge(base_synthesis, query)

        # Refine the synthesis based on the challenge (simulated)
        refined_synthesis = f"{base_synthesis} Further deepened by resolving: {challenge}"

        # Store in BrainStore for future use
        brain_store.store_wisdom(query, {
            "base_synthesis": base_synthesis,
            "challenge": challenge,
            "refined_synthesis": refined_synthesis,
            "themes": themes
        })

        return refined_synthesis

    async def consult_brain(self, query: str):
        """
        Coordinates the retrieval and synthesis process.
        """
        # 1. Check BrainStore first for pre-refined wisdom (Optimization: skip RAG if found)
        stored = brain_store.get_wisdom(query)
        if stored:
             return {
                "query": query,
                "synthesis": f"{stored['refined_synthesis']} (Retrieved from Eternal Memory)",
                "wisdom_nugget": "This wisdom is already established in our collective memory.",
                "all_fragments": [],
                "connections": [],
                "certainty": 1.0
            }

        # 2. Retrieve raw context (the 'eternal memory')
        raw_context = retrieval_service.retrieve_context(query, limit=5)

        # 3. Learn/Synthesize the specific context for this query (with Dialectical Refinement)
        synthesis_note = await self.learn_from_context(raw_context, query=query)

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
