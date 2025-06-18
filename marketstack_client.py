import requests

class MarketstackClient:
    BASE_URL = "https://api.marketstack.com/v2"
    API_KEY = "7a51f99d4e79966961b4a0e05a7a6bf7"  # Replace with your Marketstack API key

    def __init__(self):
        if not self.API_KEY:
            raise ValueError("API key is required to use the Marketstack API.")

    def _make_request(self, endpoint, params=None):
        """
        Internal method to make an API request.
        Args:
            endpoint (str): API endpoint (e.g., "/eod").
            params (dict): Query parameters for the request.
        Returns:
            dict: Parsed JSON response from the API.
        """
        url = f"{self.BASE_URL}{endpoint}"
        headers = {"Content-Type": "application/json"}
        params = params or {}
        params["access_key"] = self.API_KEY

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            raise

    def get_historical_prices(self, symbols, date_from=None, date_to=None, limit=100):
        """
        Fetch historical prices for given symbols.
        Args:
            symbols (list): List of stock ticker symbols (e.g., ["AAPL", "MSFT"]).
            date_from (str): Start date in YYYY-MM-DD format (optional).
            date_to (str): End date in YYYY-MM-DD format (optional).
            limit (int): Number of results per request (default 100).
        Returns:
            list: List of historical price data.
        """
        params = {
            "symbols": ",".join(symbols),
            "date_from": date_from,
            "date_to": date_to,
            "limit": limit,
        }
        return self._make_request("/eod", params)

    def get_intraday_data(self, symbols, interval="1hour", date_from=None, date_to=None, limit=100, after_hours=False):
        """
        Fetch intraday data for given symbols.
        Args:
            symbols (list): List of stock ticker symbols (e.g., ["AAPL", "MSFT"]).
            interval (str): Data interval (e.g., "1min", "5min"). Default is "1hour".
            date_from (str): Start date in YYYY-MM-DD format (optional).
            date_to (str): End date in YYYY-MM-DD format (optional).
            limit (int): Number of results per request (default 100).
            after_hours (bool): Include pre/post-market data (default False).
        Returns:
            list: List of intraday data.
        """
        params = {
            "symbols": ",".join(symbols),
            "interval": interval,
            "date_from": date_from,
            "date_to": date_to,
            "limit": limit,
            "after_hours": str(after_hours).lower(),
        }
        return self._make_request("/intraday", params)

    def get_ticker_info(self, ticker):
        """
        Fetch detailed information about a specific ticker.
        Args:
            ticker (str): Stock ticker symbol (e.g., "MSFT").
        Returns:
            dict: Detailed information about the ticker.
        """
        params = {"ticker": ticker}
        return self._make_request("/tickerinfo", params)

    def get_index_list(self, limit=100, offset=0):
        """
        Fetch a list of stock market indices.
        Args:
            limit (int): Number of results per request (default 100).
            offset (int): Offset for pagination (default 0).
        Returns:
            list: List of market indices.
        """
        params = {"limit": limit, "offset": offset}
        return self._make_request("/indexlist", params)

    def get_index_info(self, index):
        """
        Fetch detailed information about a specific market index.
        Args:
            index (str): Benchmark/index ID (e.g., "australia_all_ordinaries").
        Returns:
            dict: Detailed information about the market index.
        """
        params = {"index": index}
        return self._make_request("/indexinfo", params)

    def handle_error(self, error_response):
        """
        Handle API errors and return detailed error messages.
        Args:
            error_response (dict): Error response from the API.
        """
        error = error_response.get("error", {})
        code = error.get("code", "unknown_error")
        message = error.get("message", "An unknown error occurred.")
        context = error.get("context", {})
        print(f"Error Code: {code}\nMessage: {message}\nContext: {context}")