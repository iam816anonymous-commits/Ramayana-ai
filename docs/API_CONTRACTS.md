# API Contracts: Ramayana AI

## Sanctum API
`POST /api/sanctum/reflect`
- **Request:**
  ```json
  {
    "query": "What is the meaning of Dharma in exile?"
  }
  ```
- **Response:**
  ```json
  {
    "reflection": "...",
    "meaning": "...",
    "context": "...",
    "takeaway": "...",
    "type": "moral",
    "metadata": { ... }
  }
  ```

## Timeline API
`GET /api/timeline`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "title": "Birth of Rama",
      "description": "...",
      "kanda": "Bal Kanda"
    }
  ]
  ```

## Characters API (V2+)
`GET /api/characters`
`POST /api/characters/{name}/chat`
