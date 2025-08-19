from qiskit_optimization import QuadraticProgram
import pandas as pd

def qabo_transform(tickers, mu, cov, k = 2, risk_penalty = 0.5):
    """
    Construct a Qudratic Program for Portfolio Optimization using QAOA

    Args
        :param tickers: List of asset tickers
        :param mu: Expected return for each asset
        :param cov: Covariance matrix of returns
        :param k: Number of assets to select
        :param risk_penalty: Trade-off parameter between risk and return

    Returns
        :return: QudraticProgram: Qiskit optimzation program ready for solving
    """

    mu = pd.Series(mu, index=tickers) if not isinstance(mu, pd.Series) else mu
    cov = pd.DataFrame(cov, index=tickers, columns=tickers) if not isinstance(cov, pd.DataFrame) else cov

    qp = QuadraticProgram()

    # Definning binary decision variable
    for i, label in enumerate(tickers):
        qp.binary_var(f'x{i}')

    # Objective function: maximize returns - risk_penalty
    linear = {f'x{i}': mu.iloc[i] for i in range(len(tickers))}
    quadratic = {(f'x{i}',f'x{j}'): -risk_penalty * cov.iloc[i, j]
                for i in range(len(tickers))
                for j in range(len(tickers))}

    qp.maximize(linear=linear, quadratic=quadratic)

    # Adding constraints to select exactly k assests (e.g., sum x_i == 2 for choosing 2 assets)
    qp.linear_constraint(linear={f'x{i}': 1 for i in range(len(tickers))},
                         sense='==', rhs = k)

    return qp
