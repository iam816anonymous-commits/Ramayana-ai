# Database Schema: Ramayana AI

## Postgres (Relational)
- **Users (V4+):** id, email, password_hash, created_at.
- **Profiles:** user_id, name, bio, preferences.
- **Reflections:** id, user_id, query, response, context_ids, created_at.
- **DailyQuotes:** id, text, author, date.

## Qdrant (Vector)
- **Collection: `ramayana_docs`**
  - **Payload:** text, source, chapter, kanda, verse_number.
  - **Vector:** 384-dim (all-MiniLM-L6-v2).

## Neo4j (Graph)
- **Nodes:** Character, Place, Event, Weapon, Kingdom, Teaching.
- **Relationships:** RELATED_TO, BROTHER_OF, WIFE_OF, FOUGHT_IN, LOCATED_IN.

## Redis (Key-Value)
- **Sessions:** User session data.
- **Cache:** Frequent query results.
- **Rate Limiting:** IP-based limits.
