import numpy as np
from typing import List
from scipy.optimize import minimize
from simulation import run_simulation


def objective(params: List, config) -> float:
    """
    Objective function for the PID parameter optimization
    Args:
    :params (list): PID Parameters [k_p, k_i, k_d]
    :config (SimulationConfig): Simulation configuration object
    :return:
    Objective value to be minimized (float)
    """
    results = run_simulation(params, config)
    position_error = np.sum(np.abs(results['x']))
    control_forces = np.sum(np.abs(results['u']))
    # We want to penalize large control forces here
    return position_error + 0.01 * control_forces


def optimize_pid(config) -> List:
    """
    Optimize the PID Parameters
    Args:
    :config (SimulationConfig): Simulation Configuration object
    :return:
    List: optimized PID parameters [k_p, k_i, k_d]
    """
    result = minimize(
        objective,
        config.initial_pid_params,
        args=(config,),
        method="L-BFGS-B",
        bounds=config.optimization_bounds
    )
    return result.x
