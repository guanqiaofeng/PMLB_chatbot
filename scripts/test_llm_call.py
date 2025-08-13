import requests

prompt = """
You are a Labguru assistant. Given a user's message, extract the intent and any filters.

Respond in JSON only.

User: List organoids starting with 'PHLC'
"""

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama3",
    "prompt": prompt,
    "stream": False
})

print(response.json()["response"])