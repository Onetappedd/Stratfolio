import logging
from core.marketstack_client import get_stock_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

RISK_PROFILES = {
    "Conservative": {"bonds": 0.7, "stocks": 0.2, "cash": 0.1},
    "Moderately Conservative": {"bonds": 0.5, "stocks": 0.4, "cash": 0.1},
    "Moderate": {"bonds": 0.4, "stocks": 0.5, "cash": 0.1},
    "Moderately Aggressive": {"bonds": 0.2, "stocks": 0.7, "cash": 0.1},
    "Aggressive": {"bonds": 0.1, "stocks": 0.85, "cash": 0.05},
}

async def allocate_portfolio(risk_profile: str, investment_amount: float, use_api: bool = True) -> dict:
    """Allocate a portfolio based on risk profile and amount."""
    logger.info("Allocating portfolio for %s with amount %.2f", risk_profile, investment_amount)

    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero")

    if risk_profile not in RISK_PROFILES:
        raise ValueError(f"Invalid risk profile: {risk_profile}")

    allocations = RISK_PROFILES[risk_profile]
    portfolio = {
        "stocks": [],
        "bonds": [],
        "cash": round(investment_amount * allocations["cash"], 2),
    }

    stock_amount = investment_amount * allocations["stocks"]
    bond_amount = investment_amount * allocations["bonds"]

    if use_api:
        stock_symbols = ["AAPL", "MSFT", "GOOGL"]
        bond_symbols = ["BND", "AGG"]
        stock_data = await get_stock_data(stock_symbols)
        bond_data = await get_stock_data(bond_symbols)

        portfolio["stocks"] = [
            {
                "symbol": item["symbol"],
                "price": item["close"],
                "allocation": round(stock_amount / len(stock_data["data"]), 2),
            }
            for item in stock_data.get("data", [])
        ]
        portfolio["bonds"] = [
            {
                "symbol": item["symbol"],
                "price": item["close"],
                "allocation": round(bond_amount / len(bond_data["data"]), 2),
            }
            for item in bond_data.get("data", [])
        ]
    else:
        portfolio["stocks"] = [
            {"symbol": "AAPL", "price": 150, "allocation": round(stock_amount / 3, 2)},
            {"symbol": "MSFT", "price": 250, "allocation": round(stock_amount / 3, 2)},
            {"symbol": "GOOGL", "price": 2800, "allocation": round(stock_amount / 3, 2)},
        ]
        portfolio["bonds"] = [
            {"symbol": "BND", "price": 85, "allocation": round(bond_amount / 2, 2)},
            {"symbol": "AGG", "price": 110, "allocation": round(bond_amount / 2, 2)},
        ]

    logger.info("Final portfolio: %s", portfolio)
    return portfolio
