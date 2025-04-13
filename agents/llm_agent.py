import requests
import json
OLLAMA_URL="https://1315-2401-4900-1b99-ac-446-81b3-303e-bc7f.ngrok-free.app"


def query_ollama(prompt):
    payload={
        "model":"llama3.2",
        "prompt":prompt
    }

    response = requests.post(OLLAMA_URL, json=payload)
    if response.ok:
        return response.json().get("response", "No response.")
    return f"Ollama error: {response.status_code}
