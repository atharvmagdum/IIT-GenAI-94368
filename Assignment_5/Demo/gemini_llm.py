import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")
url = "https://api.generativeai.google/v1beta2/models/gemini-1.5-flash:generateContent?key{api_key}"
headers = { 
    "Content-Type": "application/json"
}

user_prompt = input("Ask anything: ")
data = {
    "contents":[
        { "parts":[{"text":user_prompt}]  }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())