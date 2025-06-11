import requests
import logging
from config import API_URL, HEADERS

def extract_data():
    try:
        response = requests.get(API_URL, headers=HEADERS)
        response.raise_for_status()
        logging.info("API call successful")
        return response.json()
    except Exception as e:
        logging.error(f"API request failed: {e}")
        return []