def generate_portfolio(risk_level, investment_amount, use_marketstack_api=False):
    """
    Generate a portfolio based on the risk level and investment amount.
    Args:
        risk_level (str): Risk level (e.g., "Moderate", "Aggressive").
        investment_amount (float): Total investment amount in USD.
        use_marketstack_api (bool): Whether to fetch data from Marketstack API.
    Returns:
        dict: Portfolio allocation with aggregated results.
    """
    # Example allocation logic (adjust as needed for risk level)
    raw_allocation = [
        {"asset_class": "Stocks", "ticker": "MSFT", "allocation": 0.25 * investment_amount},
        {"asset_class": "Stocks", "ticker": "AAPL", "allocation": 0.25 * investment_amount},
        {"asset_class": "Stocks", "ticker": "GOOGL", "allocation": 0.20 * investment_amount},
        {"asset_class": "Bonds", "ticker": "BND", "allocation": 0.20 * investment_amount},
        {"asset_class": "Bonds", "ticker": "AGG", "allocation": 0.10 * investment_amount},
        {"asset_class": "Stocks", "ticker": "MSFT", "allocation": 0.05 * investment_amount},  # Duplicate
    ]

    # Aggregate allocations for the same ticker
    aggregated_allocation = {}
    for item in raw_allocation:
        key = (item["asset_class"], item["ticker"])
        if key not in aggregated_allocation:
            aggregated_allocation[key] = item["allocation"]
        else:
            aggregated_allocation[key] += item["allocation"]

    # Convert aggregated results into a list
    final_allocation = [
        {"asset_class": key[0], "ticker": key[1], "allocation": value}
        for key, value in aggregated_allocation.items()
    ]

    # Sort allocation by asset class and ticker for better readability
    final_allocation.sort(key=lambda x: (x["asset_class"], x["ticker"]))

    return final_allocation