# Ramayana AI: The Sanctum of Mythology Intelligence

An AI-native mythology ecosystem where users can talk to characters, explore timelines, and experience the Ramayana universe through a meditative, "Temple Aesthetic" interface.

## 🏛️ Product Vision: The Sanctum
Ramayana AI is not just a chatbot; it is a **Sacred Sanctum**. The platform focuses on:
- **Character Intelligence:** Conversing with Rama, Sita, Hanuman, and others with deep persona consistency.
- **Eternal Memory:** A RAG-driven intelligence that synthesizes wisdom from thousands of sacred fragments.
- **Meditative UX:** A "Temple Aesthetic" UI designed for reflection ("Sit. Ask. Reflect.").
- **Timeline Exploration:** Navigating the major events of the Ramayana with interactive context.

## 🛠️ Technical Architecture

### Intelligence Engine (Agentic Flow)
1. **Brain Agent:** The synthesis core. It processes RAG context and Knowledge Graph relations to identify themes like *Dharma*, *Bhakti*, and *Aranya*.
2. **Sage Agent:** The formatter. It transforms raw intelligence into poetic, scriptural-style revelations.
3. **Character Engine:** Manages personas, traits, and emotional consistency for various mythological figures.

### Tech Stack
- **Frontend:** Next.js 15 (App Router), Tailwind CSS, Framer Motion (for "Temple" animations).
- **Backend:** FastAPI, Python, Qdrant (Vector DB), Neo4j (Knowledge Graph - Phase 2).
- **Ingestion:** Modular pipeline supporting PDF, JSON, and Text with automated thematic tagging.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js 20+
- Docker (for Qdrant/Neo4j)

### Installation
1. **Backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   export PYTHONPATH=$PYTHONPATH:.
   uvicorn backend.app.main:app --reload
   ```
2. **Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## 📜 Documentation
- `backend/app/agents/`: Core AI logic (Brain, Sage, Orchestrator).
- `backend/app/ingestion/`: Data processing pipelines.
- `frontend/src/components/`: Temple UI components (Diya, Pillar, Manuscript).

## 🗺️ Roadmap
- **Phase 1 (Complete):** RAG Foundation, Temple UI, Brain/Sage Agentic Flow, Basic Timeline.
- **Phase 2 (Next):** Full Knowledge Graph Integration, Regional Multi-version Support.
- **Phase 3:** Visual Story Generation, Kids Mode with Interactive Puzzles.
- **Phase 4:** Creator Ecosystem and API Marketplace.

---
*May your journey through the Sanctum be enlightened.*
