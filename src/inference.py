import joblib
import faiss
import pickle
import requests
from sentence_transformers import SentenceTransformer

ticket_clf = joblib.load("models/ticket_classifier.pkl")
priority_clf = joblib.load("models/priority_classifier.pkl")

embedder = SentenceTransformer("all-MiniLM-L6-v2")

ticket_index = faiss.read_index("vector_store/ticket_faiss.index")
kb_index = faiss.read_index("vector_store/kb_faiss.index")

with open("vector_store/ticket_metadata.pkl", "rb") as f:
    ticket_metadata = pickle.load(f)

with open("vector_store/kb_metadata.pkl", "rb") as f:
    kb_metadata = pickle.load(f)


def retrieve_similar_tickets(query, top_k=5):
    query_embedding = embedder.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")

    distances, indices = ticket_index.search(query_embedding, top_k)

    results = []

    for idx, dist in zip(indices[0], distances[0]):
        item = ticket_metadata[idx].copy()
        item["distance"] = float(dist)
        results.append(item)

    return results


def retrieve_kb(query, top_k=3):
    query_embedding = embedder.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")

    distances, indices = kb_index.search(query_embedding, top_k)

    results = []

    for idx, dist in zip(indices[0], distances[0]):
        item = kb_metadata[idx].copy()
        item["distance"] = float(dist)
        results.append(item)

    return results


def call_ollama(prompt, model="llama3.2:3b"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]


def generate_resolution(ticket, category, priority, similar_tickets, kb_results):
    similar_context = "\n\n".join([
        f"- Category: {item['category']}, Priority: {item['priority']}, Ticket: {item['ticket_text']}"
        for item in similar_tickets
    ])

    kb_context = "\n\n".join([
        f"Source: {item['source']}\n{item['content']}"
        for item in kb_results
    ])

    prompt = f"""
You are an IT service desk assistant for an enterprise managed service provider.

Ticket:
{ticket}

Predicted Category:
{category}

Predicted Priority:
{priority}

Similar Past Tickets:
{similar_context}

Knowledge Base:
{kb_context}

Generate a practical response using this format:
1. Issue Summary
2. Recommended Troubleshooting Steps
3. Suggested Escalation Team
4. Risk Note
5. Sources Used
"""

    return call_ollama(prompt)


def analyze_ticket(ticket_text):
    category = ticket_clf.predict([ticket_text])[0]
    priority = priority_clf.predict([ticket_text])[0]

    similar_tickets = retrieve_similar_tickets(ticket_text, top_k=5)
    kb_results = retrieve_kb(ticket_text, top_k=3)

    resolution = generate_resolution(
        ticket=ticket_text,
        category=category,
        priority=priority,
        similar_tickets=similar_tickets,
        kb_results=kb_results
    )

    return {
        "category": category,
        "priority": priority,
        "similar_tickets": similar_tickets,
        "kb_sources": [item["source"] for item in kb_results],
        "resolution": resolution
    }