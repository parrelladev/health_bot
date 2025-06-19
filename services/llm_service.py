import os
from typing import List
import openai


class LLMService:
    def __init__(self, api_key: str | None = None):
        openai.api_key = api_key or os.getenv("OPENAI_API_KEY")

    def generate_script(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"].strip()
