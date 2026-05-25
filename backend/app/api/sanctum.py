from fastapi import APIRouter
from pydantic import BaseModel
from backend.app.agents.orchestrator import orchestrator
from backend.app.agents.sage import SanctumResponse

router = APIRouter()

class ReflectRequest(BaseModel):
    query: str

@router.post("/reflect", response_model=SanctumResponse)
async def reflect(request: ReflectRequest):
    return await orchestrator.process_query(request.query)
