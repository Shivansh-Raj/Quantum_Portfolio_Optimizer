
from qiskit_algorithms import QAOA
# COBYLA: Constrained Optimization BY Linear Approximation
from qiskit_algorithms.optimizers import COBYLA
from qiskit_aer.primitives import Sampler
from qiskit_optimization.algorithms import MinimumEigenOptimizer


def qoao_implementation(qp, reps = 1, maxiter = 100):
    """
    Solve the given quadratic program using QAOA with COBYLA optimizer

    Args:
        :param qp: The optimization problem to solve
        :param reps: Number of qa repetition(Circuit Depth)
        :param maxiter: Maximum number of COBYLA iteration
    Returns:
        dict: {
            "selected_assets": list of chosen variable names,
            "result": full Qiskit optimization result object
        }
    """
    # Classical optimizer for QAOA parameter tuning
    optimizer = COBYLA(maxiter=maxiter)

    # Quantum Approximate optimatization Algorithm
    qaoa = QAOA(sampler=Sampler(), optimizer=optimizer ,reps = 1)

    # Wrap QAOA optimizer in a Minimum Eigen Optimizer
    optimizer = MinimumEigenOptimizer(qaoa)

    # SOlving the QP
    result = optimizer.solve(qp)

    selected_assets = [var for var, val in zip(qp.variables, result.x) if val > 0.5]

    return {
        "selected_assets": selected_assets,
        "result": result
    }

