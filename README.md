# Quantum Portfolio Optimizer

A hybrid **Quantum-Classical Portfolio Optimization** engine that selects the optimal set of assets using both **QAOA (Quantum Approximate Optimization Algorithm)** and a **classical brute-force solver**.  
The optimizer balances **expected return** and **portfolio risk** (variance) based on user-defined parameters.

---

## Features
- 🚀 **Quantum Solver (QAOA)**: Uses Qiskit's `MinimumEigenOptimizer` to solve the portfolio optimization as a QUBO.
- 🧮 **Classical Solver**: Brute-force optimizer using Python & NumPy for exact comparison.
- 📊 **Risk & Return Metrics**:
  - Expected portfolio return
  - Portfolio variance (risk)
  - Objective function value (risk-return tradeoff)
- 🔄 **API-Ready**: Accepts JSON input of tickers, number of assets to select, and solver parameters.

---

## Example Usage

### Input
```json
{
  "tickers": ["AAPL", "GOOGL", "TSLA", "MSFT"],
  "k": 2,
  "risk_penalty": 0.5,
  "reps": 1,
  "maxiter": 100
}
```

### Output
```json
{
  "quantum_result": {
    "chosen_assets": ["TSLA", "MSFT"],
    "selection_vector": [0, 0, 1, 1],
    "expected_return": 0.0037,
    "portfolio_risk": 0.0541,
    "objective_value": 0.0022
  },
  "classical_result": {
    "chosen_assets": ["TSLA", "MSFT"],
    "selection_vector": [0, 0, 1, 1],
    "expected_return": 0.0037,
    "portfolio_risk": 0.0541,
    "objective_value": 0.0022
  }
}
```

### Installation
```bash
git clone https://github.com/Shivansh-Raj/Quantum_Portfolio_Optimizer
pip install -r requirements.txt
```
### Run the Project

Navigate to the app folder
```
cd app
```

Run the main FastAPI file
```
uvicorn main:app --reload
```

This starts the server on http://127.0.0.1:8000.

Open API docs (Swagger UI)
```
Go to: http://127.0.0.1:8000/docs in your browser to interact with the endpoints.
```
