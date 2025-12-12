import os
import requests
from dotenv import load_dotenv

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
print(f"Groq Key Loaded: {bool(groq_key)}")

if groq_key:
    try:
        print("Testing Groq...")
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {groq_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "user", "content": "Hello"}],
                "max_tokens": 10
            },
            timeout=10
        )
        print(f"Groq Status: {response.status_code}")
        if response.status_code != 200:
            print(f"Groq Error: {response.text}")
        else:
            print("Groq Success!")
    except Exception as e:
        print(f"Groq Exception: {e}")

or_key = os.getenv("OPENROUTER_API_KEY")
print(f"OpenRouter Key Loaded: {bool(or_key)}")

if or_key:
    try:
        print("Testing OpenRouter...")
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {or_key}",
                "Content-Type": "application/json",
                 "HTTP-Referer": "https://test.com", 
            },
            json={
                "model": "meta-llama/llama-3.2-3b-instruct:free",
                "messages": [{"role": "user", "content": "Hello"}],
            },
            timeout=10
        )
        print(f"OpenRouter Status: {response.status_code}")
        if response.status_code != 200:
            print(f"OpenRouter Error: {response.text}")
        else:
            print("OpenRouter Success!")
    except Exception as e:
        print(f"OpenRouter Exception: {e}")
