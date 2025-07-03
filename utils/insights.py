import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Use chat-compatible interface (works with Gemini 1.5/Pro)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")  

def get_ai_insights(data: dict) -> str:
    """
    Sends processed flight data to Gemini and gets back a human-readable summary.
    """
    if not data or not isinstance(data, dict):
        return "No insights available due to missing or invalid data."

    prompt = (
        "You are an aviation market analyst. Based on the following JSON data about airline activity, "
        "write a market demand report with the following structure:\n\n"

        "Begin the report with a one-line summary of the overall market activity.\n\n"

        "1. First paragraph: Discuss the busiest flight routes, highlighting the top 2–3 routes and what this might suggest about demand between certain cities.\n"
        "2. Second paragraph: Talk about the most active airlines based on volume of flights. Mention the top airlines and what this suggests about their market presence.\n"
        "3. Third paragraph: Analyze the most common departure airports. Mention the most active airports and any insights about their geographic importance.\n"
        "4. Fourth paragraph: Discuss the most common arrival airports, highlighting key destinations and possible tourist or business trends.\n"
        "5. Final paragraph: Using your knowledge of recent aviation trends and internet-based pricing information, summarize the current price trends across the most active routes and airlines mentioned above. "
        "You may include commentary on whether prices are rising or falling for major domestic and international routes, and explain possible reasons for these trends.\n\n"

        "Ensure the report is written in a clear, professional tone. Use plain English and avoid bullet points. Keep each paragraph focused and insightful.\n\n"
        "Here is the data in JSON format:\n\n"
        f"{json.dumps(data, indent=2)}"
    )


    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Error while generating AI insights:", e)
        return "Unable to generate AI insights at the moment."
