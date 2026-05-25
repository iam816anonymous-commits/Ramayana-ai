from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import characters, timeline, sanctum, daily
from app.ingestion.pipeline import ingestion_pipeline

app = FastAPI(title="Ramayana AI API")

@app.on_event("startup")
async def startup_event():
    print("Starting auto-discovery and ingestion...")
    ingestion_pipeline.scan_data_folder()

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
app.include_router(daily.router, prefix="/api/daily", tags=["daily"])

@app.get("/")
async def root():
    return {"message": "Welcome to Ramayana AI API"}
