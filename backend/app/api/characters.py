from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.character_service import chat_service

router = APIRouter()

class ChatRequest(BaseModel):
    character: str
    message: str

class ChatResponse(BaseModel):
    character: str
    response: str

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response_text = await chat_service.get_response(request.character, request.message)
    return ChatResponse(character=request.character, response=response_text)
