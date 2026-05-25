
import requests
from config import OLLAMA_BASE_URL, OLLAMA_MODEL

def get_embedding(text):
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/embed",
        json={
            "model": OLLAMA_MODEL,
            "input": text
        }
    )

    response.raise_for_status()

    data = response.json()

    return data["embeddings"][0]