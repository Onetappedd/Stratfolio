import os
import logging
import httpx

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://api.marketstack.com/v1"

async def get_stock_data(symbols: list[str]) -> dict:
    """Fetch stock data from the Marketstack API for the given ticker symbols."""
    api_key = os.getenv("MARKETSTACK_API_KEY")
    if not api_key:
        raise EnvironmentError("MARKETSTACK_API_KEY environment variable not set")

    endpoint = f"{BASE_URL}/eod"
    params = {"access_key": api_key, "symbols": ",".join(symbols)}
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint, params=params)
    logger.info("Marketstack API Response: %s - %s", response.status_code, response.text)
    response.raise_for_status()
    data = response.json()
    if "error" in data:
        raise ValueError(f"Marketstack API error: {data['error']['message']}")
    return data
