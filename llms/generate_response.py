import os
import json
import asyncio
import requests

from typing import List, Dict, Any, Optional, Callable, Union
from dotenv import load_dotenv
load_dotenv()
class LLMResponseGenerator:
    def __init__(self, api_url: str = os.getenv("TEXT_API_URL"), api_key: str):
        self.api_url = api_url
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }


    def generate_text_response(self, prompt: str, model: str = "gemini-2.0-flash", **kwargs) -> str:
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            **kwargs
        }
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        else:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


    def generate_image_response(self, prompt: str, n: int = 1, size: str = "1024x1024") -> List[str]:
        payload = {
            "prompt": prompt,
            "n": n,
            "size": size
        }
        response = requests.post(f"{self.api_url}/images/generations", headers=self.headers, json=payload)
        if response.status_code == 200:
            return [data.get("url") for data in response.json().get("data", [])]
        else:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")