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
    try:
        response = text_llm.generate_text_response(prompt=prompt, model="gemini-2.0-flash", temperature=0.3, max_tokens=500)

    except Exception as e:
        st.error(f"Error fetching news: {e.__traceback__.tb_lineno} {str(e)}")

    return response


def generate_video_transcription(prompt):
    """Generate video transcription based on a prompt."""
    text_llm = LLMResponseGenerator(api_url=os.getenv("TEXT_API_URL"), api_key=os.getenv("EURI_API_KEY"))
    prompt = f"""
You are a creative script writing AI specialized in generating engaging video scripts for YouTube shorts or Instagram reels. Write in a natural speaking style, using simple language with hook at the beginning to grab attention and CTA at the end. Keep the script concise and engaging, around 150-200 words. Use a friendly and conversational tone, as if speaking directly to the viewer. Avoid jargon and complex terms to ensure clarity and relatability.
news text: {news_texts}
    """
    try:
        response = text_llm.generate_text_response(prompt=prompt, model="gpt-4.1-mini", temperature=0.3, max_tokens=500)

    except Exception as e:
        st.error(f"Error generating transcription: {e.__traceback__.tb_lineno} {str(e)}")

    return response

# if __name__ == "__main__":
#     st.title("Real-Time News Fetcher")
#     st.write("Enter a topic to fetch the latest news articles.")

#     query = st.text_input("News Topic", "Artificial Intelligence")

#     if st.button("Fetch News"):
#         with st.spinner("Fetching news..."):
#             try:
#                 news = fetch_news(query)
#                 st.subheader("Latest News:")
#                 st.write(news)
#             except Exception as e:
#                 st.error(f"Error fetching news: {e.__traceback__.tb_lineno} {str(e)}")