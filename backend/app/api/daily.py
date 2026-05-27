from fastapi import APIRouter
from app.ingestion.pipeline import ingestion_pipeline

router = APIRouter()

@router.post("/reindex")
async def reindex():
    """Manually trigger a full re-ingestion of local data."""
    print("Manual re-indexing triggered...")
    ingestion_pipeline.scan_data_folder(reset=True)
    return {"status": "success", "message": "Re-indexing complete"}

@router.get("/quote")
async def get_daily_quote():
    # Future: Fetch from DB
    return {"quote": "Dharma is the foundation of the universe.", "author": "Valmiki"}

@router.get("/wisdom")
async def get_daily_wisdom():
    return {"wisdom": "The path of duty is the way to glory."}

@router.get("/health")
async def health():
    return {"status": "healthy", "service": "daily"}
