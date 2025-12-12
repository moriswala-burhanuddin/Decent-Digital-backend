import requests

keys = [
    "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", # Gemini Flash
    "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"  # Phi
]

def test_key(key):
    print(f"Testing key: {key[:15]}...")
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://test.com", 
            },
            json={
                "model": "google/gemini-2.0-flash-exp:free", # Trying a free model
                "messages": [{"role": "user", "content": "Hello"}],
            },
            timeout=10
        )
        if response.status_code == 200:
            print(f"SUCCESS! Key {key[:15]}... works.")
            return True
        else:
            print(f"FAILED. Status: {response.status_code}, Response: {response.text}")
            return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

for key in keys:
    if test_key(key):
        break
