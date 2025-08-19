import numpy as np

def filter_result(result, tickers, mu, cov, risk_penalty):
    selected_assets = safe_to_list(result.x)
    objective_val = safe_to_list(result.fval)
    # raw_solver = safe_to_list(result.min_eigen_solver_result)
    # print(type(selected_assets),"-----",objective_val,"------",raw_solver)

    trading_days = 252

    chosen = [tickers[i] for i, v in enumerate(selected_assets) if v == 1]

    expected_return = float(np.dot(mu, selected_assets) * trading_days)

    portfolio_var = float(np.dot(selected_assets, np.dot(cov, selected_assets)))
    portfolio_risk = float(np.sqrt(portfolio_var) * np.sqrt(trading_days))

    objective_val = expected_return - risk_penalty * portfolio_risk

    return {
        "chosen_assets": chosen,
        "selection_vector": selected_assets,
        "expected_return": expected_return,
        "portfolio_risk": portfolio_risk,
        "objective_value": objective_val
    }



def safe_to_list(obj):
    return obj.tolist() if isinstance(obj, np.ndarray) else obj