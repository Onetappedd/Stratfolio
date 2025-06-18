import requests
import logging

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
MARKETSTACK_API_KEY = "7a51f99d4e79966961b4a0e05a7a6bf7"  # Replace with your actual API key
BASE_URL = "https://api.marketstack.com/v1"

def get_stock_data(symbols):
    """
    Fetch stock data for the given symbols from the Marketstack API.

    Args:
        symbols (list): List of stock ticker symbols.

    Returns:
        dict: Parsed JSON response containing stock data.

    Raises:
        Exception: If the API returns an error or invalid symbols are provided.
    """
    logger.info(f"Fetching stock data for symbols: {symbols}")
    try:
        endpoint = f"{BASE_URL}/eod"
        params = {
            "access_key": MARKETSTACK_API_KEY,
            "symbols": ",".join(symbols)
        }
        response = requests.get(endpoint, params=params)

        # Log response
        logger.info(f"Marketstack API Response: {response.status_code} - {response.text}")
        response.raise_for_status()  # Raise exception for HTTP errors

        data = response.json()
        if "error" in data:
            raise ValueError(f"Marketstack API error: {data['error']['message']}")

        return data

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching stock data: {e}")
        raise Exception(f"Marketstack API error: {e}")