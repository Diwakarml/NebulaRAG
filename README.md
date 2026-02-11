# NebulaRAG

NebulaRAG is a lightweight Retrieval-Augmented Generation (RAG) system that enables semantic search and question answering over user-provided documents. The system is designed to run entirely on free and open-source components, using local embeddings and optional external LLM inference.

The focus of this implementation is simplicity, correctness, and clear separation of concerns rather than feature completeness.

---

## Design Goals

- Zero dependency on paid embedding APIs
- Clear ingestion → embedding → retrieval → generation pipeline
- Fast local semantic search
- Easy to reason about and extend
- Minimal infrastructure complexity

---

## Architecture Overview

- **Frontend:** HTML/CSS/JS Aero-Glass UI served by FastAPI  
- **Backend:** FastAPI application coordinating ingestion and querying  
- **Embeddings:** `sentence-transformers` (`all-MiniLM-L6-v2`) running locally  
- **Vector Store:** Endee-backed in-memory similarity search  
- **LLM:** Local mock (default) or Groq Llama 3.3 (free tier)

---

## Role of Endee

Endee is used as a lightweight vector similarity layer to store and retrieve document embeddings during query time. In this implementation, Endee is intentionally used in an in-memory configuration to keep the system simple and focused on retrieval correctness rather than persistence.

This keeps the system easy to debug and reason about while still demonstrating proper vector-based retrieval.

---

## Why These Choices

- Local embeddings keep data private and eliminate API cost
- Endee provides a clean abstraction for vector similarity search without requiring external infrastructure
- In-memory configuration avoids unnecessary database setup for a task-focused implementation
- Provider-based LLM abstraction allows switching between local mock and Groq without refactoring core logic

---

## Running the Project

```bash
pip install -r requirements.txt
python app/main.py

The application will be available at:

http://localhost:8002
