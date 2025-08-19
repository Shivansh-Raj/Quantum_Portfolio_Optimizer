from pydantic import BaseModel
from typing import List

class PortfolioRequest(BaseModel):
    tickers: List[str] = ["MSFT", "AAPL", "GOOGL", "TSLA"]
    k: int = 2
    risk_penalty: float = 0.5
    reps: int = 1
    maxiter: int = 100