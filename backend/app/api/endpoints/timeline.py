from fastapi import APIRouter

router = APIRouter()

TIMELINE_EVENTS = [
    {"id": 1, "title": "Birth of Rama", "description": "Rama is born in Ayodhya to King Dasharatha.", "kanda": "Bal Kanda"},
    {"id": 2, "title": "Breaking Shiva's Bow", "description": "Rama lifts and breaks the heavy bow of Shiva in Mithila to win Sita's hand.", "kanda": "Bal Kanda"},
    {"id": 3, "title": "The Exile", "description": "Rama is exiled to the forest for 14 years due to Kaikeyi's boons.", "kanda": "Ayodhya Kanda"},
    {"id": 4, "title": "Bharata's Return", "description": "Bharata visits Rama in the forest and returns with his sandals.", "kanda": "Ayodhya Kanda"},
]

@router.get("/")
async def get_timeline():
    return TIMELINE_EVENTS
