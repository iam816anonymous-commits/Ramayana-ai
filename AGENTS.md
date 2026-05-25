# Agent Instructions for Ramayana AI

## Coding Standards & Philosophy

### 1. The "Temple" Aesthetic
- **UI Consistency:** Any new frontend components must adhere to the "Temple Aesthetic." Use `font-serif` for primary text, deep obsidian backgrounds (`#0a0a0a`), and gold/copper accents.
- **Micro-interactions:** Use Framer Motion for subtle "flicker" (Diya) or "fade-in" (Revelation) effects.

### 2. Backend Agentic Flow
- **Brain before Sage:** All philosophical queries should pass through the `BrainAgent` for synthesis before being formatted by the `SageAgent`.
- **Thematic Integrity:** Ensure the `BrainAgent` thematic tagging (`Dharma`, `Bhakti`, etc.) is maintained and expanded.

### 3. Data Ingestion
- **Deterministic Chunking:** Use the standard chunking pipeline to ensure context fragments remain consistent across rebuilds.
- **Source Attestation:** Always include metadata (source, version, chapter) when ingesting new texts.

## Technical Commands

### Running the System
- **Backend:** `export PYTHONPATH=$PYTHONPATH:. && uvicorn backend.app.main:app`
- **Frontend:** `npm run dev`
- **Qdrant:** (Ensure local instance is running on port 6333)

### Verification
- Always run `scripts/verify_backend_v2.py` (or latest) after modifying core RAG logic.
- Use Playwright to capture screenshots of UI changes to ensure the "Temple" aesthetic is preserved.

## Future Milestones
- **Neo4j Integration:** The `knowledge_graph.py` is currently a placeholder. Phase 2 requires a full graph schema mapping characters to events and philosophy.
- **Multi-versioning:** When implementing different versions (Valmiki vs. Tulsidas), ensure the `MultiVersionEngine` can compare fragments side-by-side.
