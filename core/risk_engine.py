def get_asset_allocation(risk_level: int, horizon_years: int | None = None):
    # Risk level mapping (1–5) to asset weights
    risk_buckets = {
        1: {"stocks": 0.2, "bonds": 0.6, "cash": 0.2},
        3: {"stocks": 0.6, "bonds": 0.3, "cash": 0.1},
        5: {"stocks": 0.9, "bonds": 0.05, "cash": 0.05},
    }
    allocation = risk_buckets.get(risk_level, risk_buckets[3])

    # Adjust based on time horizon (e.g., "120 - age" rule for stocks)
    if horizon_years:
        allocation["stocks"] += horizon_years * 0.01
        allocation["bonds"] -= horizon_years * 0.01

    return allocation