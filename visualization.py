import numpy as np
from typing import Dict
import matplotlib.pyplot as plt
from config import SimulationConfig


def plot_results(results: Dict, config: SimulationConfig) -> None:
    """
    :results (dict): Simulation results which are position, velocity, acceleration and forces
    :config (SimulationConfig): Simulation Configuration object
    :return:
    """
    # Obtain a certain number of simulation steps
    t = np.arange(0, config.T*config.dt, config.dt)

    plt.figure(figsize=(12, 10))
    plt.subplot(511)
    plt.plot(t, results['x'])
    plt.title('Particle Position')
    plt.ylabel('Position')

    plt.subplot(512)
    plt.plot(t, results['v'])
    plt.title('Particle Velocity')
    plt.ylabel('Velocity')

    plt.subplot(513)
    plt.plot(t, results['a'])
    plt.title('Particle Acceleration')
    plt.ylabel('Acceleration')

    plt.subplot(514)
    plt.plot(t, results['e'], label='Disruptive Force', alpha=0.7)
    plt.plot(t, results['u'], label='Control Force', alpha=0.7)
    plt.title('Forces')
    plt.ylabel('Force')
    plt.legend()

    plt.subplot(515)
    plt.plot(t, np.abs(results['x']))
    plt.title('Absolute Error')
    plt.xlabel('Time')
    plt.ylabel('|Error|')

    plt.tight_layout()
    plt.show()
