import os
import json
import streamlit as st

from llms.generate_response import LLMResponseGenerator
from dotenv import load_dotenv
load_dotenv()

def fetch_news(query):
    """Fetch news articles based on a query."""
    prompt = f"""
    You are a news aggregator bot and you have live real-time access to news articles. Your job is to fetch the latest news articles based on the user's query.
    Find and report the latest real-world news update about: {query}
    Keep it factual, current and professional. Summarize in around 150-200 words. Start immediately with the news content, no greetings or introductions.
    If no recent news is available say "No recent news available on this topic {query}"
    """

    text_llm = LLMResponseGenerator(api_url=os.getenv("TEXT_API_URL"), api_key=os.getenv("EURI_API_KEY"))

    response = text_llm.generate_text_response(prompt=prompt, model="gemini-2.0-flash", temperature=0.3, max_tokens=500)