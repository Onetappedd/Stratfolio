from core.marketstack_client import get_stock_data
import logging

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def allocate_portfolio(risk_profile, investment_amount, use_api=True):
    """
    Allocate portfolio based on risk profile, investment amount, and API usage.

    Args:
        risk_profile (str): User's selected risk profile (e.g., "Moderate").
        investment_amount (float): Total investment amount in dollars.
        use_api (bool): Whether to use the Marketstack API for data.

    Returns:
        dict: Allocation details with specific stocks and bonds.
    """
    logger.info(f"Allocating portfolio for risk profile: {risk_profile}, amount: {investment_amount}, use_api: {use_api}")

    # Define allocation percentages for each risk profile
    risk_profiles = {
        "Conservative": {"bonds": 0.7, "stocks": 0.2, "cash": 0.1},
        "Moderately Conservative": {"bonds": 0.5, "stocks": 0.4, "cash": 0.1},
        "Moderate": {"bonds": 0.4, "stocks": 0.5, "cash": 0.1},
        "Moderately Aggressive": {"bonds": 0.2, "stocks": 0.7, "cash": 0.1},
        "Aggressive": {"bonds": 0.1, "stocks": 0.85, "cash": 0.05},
    }

    if risk_profile not in risk_profiles:
        error_message = f"Invalid risk profile: {risk_profile}"
        logger.error(error_message)
        raise ValueError(error_message)

    allocations = risk_profiles[risk_profile]
    portfolio = {
        "stocks": [],
        "bonds": [],
        "cash": round(investment_amount * allocations["cash"], 2),
    }

    stock_amount = investment_amount * allocations["stocks"]
    bond_amount = investment_amount * allocations["bonds"]

    if use_api:
        # Use Marketstack API to fetch stock and bond data
        stock_symbols = ["AAPL", "MSFT", "GOOGL"]
        bond_symbols = ["BND", "AGG"]

        try:
            stock_data = get_stock_data(stock_symbols)
            bond_data = get_stock_data(bond_symbols)

            portfolio["stocks"] = [
                {
                    "symbol": stock["symbol"],
                    "price": stock["close"],
                    "allocation": round(stock_amount / len(stock_data["data"]), 2),
                }
                for stock in stock_data.get("data", [])
            ]
            portfolio["bonds"] = [
                {
                    "symbol": bond["symbol"],
                    "price": bond["close"],
                    "allocation": round(bond_amount / len(bond_data["data"]), 2),
                }
                for bond in bond_data.get("data", [])
            ]
        except Exception as e:
            logger.warning(f"Failed to fetch data from API. Error: {e}")
            raise

    else:
        # Use static data
        portfolio["stocks"] = [
            {"symbol": "AAPL", "price": 150, "allocation": round(stock_amount / 3, 2)},
            {"symbol": "MSFT", "price": 250, "allocation": round(stock_amount / 3, 2)},
            {"symbol": "GOOGL", "price": 2800, "allocation": round(stock_amount / 3, 2)},
        ]
        portfolio["bonds"] = [
            {"symbol": "BND", "price": 85, "allocation": round(bond_amount / 2, 2)},
            {"symbol": "AGG", "price": 110, "allocation": round(bond_amount / 2, 2)},
        ]

    logger.info(f"Final portfolio: {portfolio}")
    return portfolio