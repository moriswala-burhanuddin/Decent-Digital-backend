import requests
import zipfile
import io
import os
import base64
import json

# Create a dummy zip file in memory
def create_test_zip():
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zf:
        zf.writestr('greet.txt', 'hello')
    buffer.seek(0)
    return buffer

def test_api():
    print("Creating test ZIP...")
    zip_buffer = create_test_zip()
    
    url = 'http://127.0.0.1:8000/api/ai-edit/'
    files = {'project_zip': ('test.zip', zip_buffer, 'application/zip')}
    data = {'instructions': 'Change content of greet.txt to "HELLO WORLD"'}
    
    print("Sending request to backend...")
    try:
        response = requests.post(url, files=files, data=data)
        
        if response.status_code == 200:
            print("Success! Received response.")
            try:
                result = response.json()
                
                print(f"Has Log: {len(result.get('logs', '')) > 0}")
                print(f"Has Files: {len(result.get('files', {})) > 0}")
                
                # Verify paths start with /
                files = result.get('files', {})
                all_start_with_slash = all(k.startswith('/') for k in files.keys())
                print(f"All paths start with /: {all_start_with_slash}")
                if not all_start_with_slash:
                    print("Example keys:", list(files.keys())[:5])
                
                if all_start_with_slash:
                    print("VERIFICATION PASSED: File paths are correct for Sandpack.")
                else:
                    print("VERIFICATION FAILED: Paths do not start with /")
                    
            except Exception as e:
                print(f"Error parsing response: {e}")
        else:
            print(f"Error: Status code {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"Connection Error: {e}")
        print("Ensure Django server is running.")

if __name__ == "__main__":
    test_api()
