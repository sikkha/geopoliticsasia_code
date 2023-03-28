import requests
import os

# Set your OpenAI API key as an environment variable or replace it in the header
#api_key = os.environ.get("OPENAI_API_KEY", "your_api_key_here")
openai.api_key = "YOUR_API_KEY"
headers = {
#    "Authorization": f"Bearer {api_key}"
    "Authorization": f"Bearer {openai.api_key}"
}

response = requests.get("https://api.openai.com/v1/models", headers=headers)

if response.status_code == 200:
    models = response.json()['data']
    print("Available models:")
    for model in models:
        print(model['id'])
else:
    print("Error:", response.status_code, response.text)
