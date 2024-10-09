import argparse
import logging
from simulation import run_simulation
from optimization import optimize_pid
from visualization import plot_results
from config import SimulationConfig


def parse_arguments():
    parser = argparse.ArgumentParser(description="PID-controlled Particle Motion Simulator")
    parser.add_argument("--config", type=str, default="config.ini", help="Path to configuration file")
    parser.add_argument("--optimize", action="store_true", help="Optimize PID parameters")
    return parser.parse_args()


def main():
    args = parse_arguments()
    config = SimulationConfig(args.config)

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    if args.optimize:
        logger.info("Optimizing PID Parameters....")
        optimal_params = optimize_pid(config)
        logger.info(f"Optimal PID parameters: Kp={optimal_params[0]:.4f}, "
                    f"Ki={optimal_params[1]:.4f}, Kd={optimal_params[2]:.4f}")
    else:
        optimal_params = config.initial_pid_params

    logger.info("Running Simulation.....")
    results = run_simulation(optimal_params, config)

    logger.info("Plotting Results....")
    plot_results(results, config)

    logger.info("Simulation success")


if __name__ == '__main__':
    main()
