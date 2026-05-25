from fastapi import APIRouter

router = APIRouter()

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
