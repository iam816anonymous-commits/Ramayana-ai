from fastapi import APIRouter

router = APIRouter()

TIMELINE_EVENTS = [
    {"id": 1, "title": "Birth of Rama", "description": "Rama is born in Ayodhya to King Dasharatha.", "kanda": "Bal Kanda"},
    {"id": 2, "title": "Breaking Shiva's Bow", "description": "Rama lifts and breaks the heavy bow of Shiva in Mithila to win Sita's hand.", "kanda": "Bal Kanda"},
    {"id": 3, "title": "The Exile", "description": "Rama is exiled to the forest for 14 years due to Kaikeyi's boons.", "kanda": "Ayodhya Kanda"},
    {"id": 4, "title": "The Golden Deer", "description": "Maricha takes the form of a golden deer to lure Rama away from the hut.", "kanda": "Aranya Kanda"},
    {"id": 5, "title": "Abduction of Sita", "description": "Ravana abducts Sita from the forest and takes her to Lanka.", "kanda": "Aranya Kanda"},
    {"id": 6, "title": "Hanuman's Journey", "description": "Hanuman crosses the ocean to find Sita in Lanka.", "kanda": "Sundara Kanda"},
    {"id": 7, "title": "Building the Bridge", "description": "The Vanara army builds a bridge of stones across the ocean to Lanka.", "kanda": "Yuddha Kanda"},
    {"id": 8, "title": "The Great War", "description": "Rama defeats Ravana and his army in a fierce battle.", "kanda": "Yuddha Kanda"},
    {"id": 9, "title": "Return to Ayodhya", "description": "Rama, Sita, and Lakshmana return to Ayodhya and Rama is crowned King.", "kanda": "Uttara Kanda"},
]

@router.get("/")
async def get_timeline():
    return TIMELINE_EVENTS
