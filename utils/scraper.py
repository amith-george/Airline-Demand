import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
BASE_URL = "https://api.aviationstack.com/v1/flights"

def fetch_flight_data(limit=100):
    """
    Fetches real-time flight data from the Aviationstack API.

    Args:
        limit (int): Number of results to return.

    Returns:
        list: List of flight dictionaries or an empty list if request fails.
    """
    params = {
        'access_key': API_KEY,
        'limit': limit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if 'data' in data:
            return data['data']
        else:
            print("API returned no data:", data)
            return []

    except requests.RequestException as e:
        print("Error fetching data from Aviationstack:", e)
        return []
