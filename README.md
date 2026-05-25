#  RAG Chat Assistant

A Retrieval-Augmented Generation (RAG) chatbot built with Python, Ollama, PostgreSQL + pgvector, and Groq API.

The system ingests PDF documents, stores semantic embeddings in PostgreSQL, retrieves relevant context using vector similarity search, and generates grounded AI responses.

---

#  Tech Stack

- Python
- Ollama (`nomic-embed-text`)
- Groq API (`llama-3.1-8b-instant`)
- PostgreSQL
- pgvector
- pypdf

---

#  Project Structure

```text
pdf-rag-chat/
├── src/
│   ├── ingest.py
│   ├── chat.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── retriever.py
│   ├── generator.py
│   ├── config.py
│   └── db.py
│
├── data/
│   └── sample.pdf
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🗄 PostgreSQL + pgvector Setup

Create database:

```sql
CREATE DATABASE rag_db;
```

Enable pgvector:

```sql
CREATE EXTENSION vector;
```

Create chunks table:

```sql
CREATE TABLE chunks (
    id SERIAL PRIMARY KEY,
    text TEXT,
    embedding VECTOR(768),
    source TEXT
);
```

---

# ⚙️ Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=

GROQ_MODEL=llama-3.1-8b-instant

OLLAMA_MODEL=nomic-embed-text
OLLAMA_BASE_URL=http://localhost:11434

CHUNK_SIZE=500
CHUNK_OVERLAP=50
TOP_K=5

DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/rag_db
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Install Ollama Model

```bash
ollama pull nomic-embed-text
```

---

# 📄 Ingest PDF Documents

Place PDFs inside:

```text
data/
```

Run ingestion:

```bash
python src/ingest.py data/sample.pdf
```

Expected output:

```text
Loading PDF...
Chunking text...
Embedding and storing chunks...
Done. 39 chunks stored.
```

---

# 💬 Run Chatbot

```bash
python src/chat.py
```

Example:

```text
Ready. Ask your questions (type 'exit' to quit).

You: What is this document about?
Assistant: ...
```

---

# 🧠 System Workflow

```text
PDF
→ Chunking
→ Embeddings
→ PostgreSQL + pgvector
→ Similarity Search
→ Groq Generation
→ Final Response
```

---

# 📚 Core Components

| File | Responsibility |
|---|---|
| `ingest.py` | PDF ingestion pipeline |
| `chat.py` | Interactive chatbot |
| `chunker.py` | Manual text chunking |
| `embedder.py` | Ollama embedding generation |
| `retriever.py` | pgvector similarity search |
| `generator.py` | Groq response generation |
| `config.py` | Centralized configuration |

---

# ✅ Features

- Manual chunking with overlap
- Semantic vector search
- PostgreSQL + pgvector integration
- Ollama embeddings
- Groq-powered responses
- Context-grounded answers
- Clean separation of ingestion and chat workflows

---

# ❓ Design Decisions

### Why separate ingestion from chat?

Embedding documents is expensive and only needs to happen once.

### Why does `chat.py` also generate embeddings?

User questions must also be converted into vectors for similarity search.

### Why chunk overlap?

Overlap preserves context between neighboring chunks.

### How does retrieval work?

pgvector compares embeddings using cosine similarity distance.

---

# 👨‍💻 Author

Anord Jailos Mfilinge
