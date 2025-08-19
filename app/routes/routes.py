from fastapi import APIRouter
from app.models.request_models import PortfolioRequest
from app.services.qaoa_optimizer import solve_qaoa
from app.services.classical_optimizer import solve_classical

router = APIRouter(
    tags=["Portfolio Optimization"],
    prefix="/optimization"
)

@router.post("/")
def optimize_portfolio(request:PortfolioRequest):
    quantum_result = solve_qaoa(request.tickers, request.k)
    return {"method": "QAOA", "result": quantum_result}


@router.post("/compare")
def compare_methods(request: PortfolioRequest):
    quantum_result = solve_qaoa(request.tickers, request.k)
    classical_result = solve_classical(request.tickers, request.k, request.risk_penalty)
    return {
        "quantum_result": quantum_result,
        "classical_result" : classical_result
    }
