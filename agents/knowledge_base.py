import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_web_insight(query):
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {os.getenv('TAVILY_API_KEY')}"}
    payload = {
        "query": query,
        "search_depth": "advanced",
        "include_answer": True
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()["answer"] if response.ok else "No web insight available."
