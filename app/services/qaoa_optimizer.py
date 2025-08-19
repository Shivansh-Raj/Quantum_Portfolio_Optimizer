from .data_fetcher import fetch_data
from .result_filter import filter_result
from app.Qiskit_Dependencies.qabo_transformer import qabo_transform
from app.Qiskit_Dependencies.qaoa_solver import qoao_implementation
import numpy as np

def solve_qaoa(tickers, k, risk_penalty = 0.5, reps = 1, maxiter = 100):
    """
    Runs the complete QAOA-based portfolio optimization pipeline.

    Args:
        tickers (list[str]): Stock tickers to consider.
        k (int): Number of assets to select.
        risk_penalty (float): Weight for risk term in optimization.
        reps (int): QAOA circuit depth (number of repetitions).
        maxiter (int): Max iterations for COBYLA optimizer.

    Returns:
        dict: {
            "selected_assets": list of chosen assets,
            "raw_result": Qiskit OptimizationResult,
            "mu": expected returns,
            "cov": covariance matrix
        }
    """
    # 1. Fetching stock data
    mu, cov = fetch_data(tickers=tickers)

    # 2. Getting QUBO equation
    qp = qabo_transform(tickers, mu, cov, k, risk_penalty)

    # 3. Solving the QUBO using QAOA
    solution = qoao_implementation(qp, reps, maxiter)

    result = solution["result"]
    filtered_result= filter_result(result, tickers, mu, cov, risk_penalty)


    return filtered_result
