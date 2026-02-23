import os
import requests
from dotenv import load_dotenv

load_dotenv()

NIM_ENDPOINT = os.getenv("NIM_ENDPOINT")

def query_nim(prompt):
    payload = {
        "model": "llama3",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }

    r = requests.post(NIM_ENDPOINT, json=payload, timeout=30)
    return r.json()["choices"][0]["message"]["content"]