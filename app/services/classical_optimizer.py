
import itertools
import numpy as np
from .data_fetcher import fetch_data

def solve_classical(tickers, k, risk_penalty = 0.5):
    mu, cov = fetch_data(tickers)
    n = len(tickers)
    best_val = -1
    best_subset = None

    for combo in itertools.combinations(range(n), k):
        x = np.zeros(n)
        x[list(combo)] = 1
        trading_days = 252

        exp_return = np.dot(mu, x) * trading_days
        risk = np.sqrt(np.dot(x, np.dot(cov, x))) * np.sqrt(trading_days)

        val = exp_return - risk * risk_penalty

        if val > best_val:
            best_val = val
            best_subset = x

    chosen = [tickers[i] for i, v in enumerate(best_subset) if v == 1]

    return {
        "method": "Classical",
        "result": {
            "chosen_assets": chosen,
            "selection_vector": best_subset.tolist(),
            "expected_return": float(np.dot(mu, best_subset) * 252),
            "portfolio_risk": float(np.sqrt(np.dot(best_subset, np.dot(cov, best_subset))) * np.sqrt(252)),
            "objective_value": float(best_val)
        }
    }

