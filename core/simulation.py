import numpy as np

def run_simulation(allocations):
    # Example Monte Carlo simulation
    simulated_returns = []
    for _ in range(1000):
        total_return = sum(
            np.random.normal(0.07, 0.15) * alloc["amount"] for alloc in allocations
        )
        simulated_returns.append(total_return)

    # Calculate risk metrics
    metrics = {
        "expReturn": np.mean(simulated_returns),
        "volatility": np.std(simulated_returns),
        "VaR": np.percentile(simulated_returns, 5),
    }
    return metrics