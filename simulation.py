import numpy as np
from typing import Any, List, Dict
from pid_controller import DelayedPIDController


def run_simulation(pid_params: List, config) -> Dict[str, Any]:
    """
    Run the particle motion simulation with given PID parameters and configuration
    :param pid_params: PID parameters [Kp, Ki, Kd]
    :param config: Simulation configuration object
    :return: Simulation results including position, velocity, acceleration and forces
    """
    k_p, k_i, k_d = pid_params
    pid = DelayedPIDController(k_p, k_i, k_d, int(config.delay_time/config.dt), config.max_force)

    x = np.zeros(config.T)  # Position
    v = np.zeros(config.T)  # Velocity
    a = np.zeros(config.T)  # Acceleration
    e = np.random.randn(config.T) * 5.0  # Random disruptive force
    u = np.zeros(config.T)  # Control Force/Reactive force

    for i in range(1, config.T):
        # The error is negative of the position since the target is x = 0
        error = -x[i-1]
        u[i] = pid.calculate(error)

        # The following equations apply to a particle being simulated
        # F = m * a and with unit mass, a = F = e + u
        # v = u + a * dt
        # x = x_0 + 0.5*a*t ** 2
        # Update acceleration
        a[i] = e[i] + u[i]
        # Update velocity
        v[i] = v[i-1] + a[i] * config.dt
        # Update position
        x[i] = x[i-1] + v[i-1] * config.dt + 0.5 * a[i] * config.dt ** 2
    return {'x': x,
            'v': v,
            'a': a,
            'e': e,
            'u': u}
