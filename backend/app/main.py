from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api import characters, timeline, sanctum

app = FastAPI(title="Ramayana AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sanctum.router, prefix="/api/sanctum", tags=["sanctum"])
app.include_router(characters.router, prefix="/api/characters", tags=["characters"])
app.include_router(timeline.router, prefix="/api/timeline", tags=["timeline"])

@app.get("/")
async def root():
    return {"message": "Welcome to Ramayana AI API"}
