# Particle Motion Simulation with PID Control

## Overview

This project implements a simulation of a particle's motion in one dimension, 
controlled by a PID (Proportional-Integral-Derivative) controller. 
The simulation aims to keep the particle as close as possible to its starting point in the presence of 
a variable disruptive force.

## Features

- One-dimensional particle motion simulation
- Delayed PID controller implementation
- Configurable simulation parameters
- Optimization of PID parameters
- Visualization of simulation results

## Requirements

- Python 3.10 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/particle-motion-simulation.git
   cd particle-motion-simulation
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Configure the simulation parameters in `config.ini`.

2. Run the main simulation:
   ```
   python main.py
   ```

3. To run the simulation with PID parameter optimization:
   ```
   python main.py --optimize
   ```

## Configuration

Edit `config.ini` to modify simulation parameters:

- `dt`: Time step
- `T`: Total number of time steps
- `delay_time`: Delay in the PID controller response
- `max_force`: Maximum force the controller can apply
- Initial PID parameters (Kp, Ki, Kd)
- Optimization bounds for PID parameters

## Project Structure

- `main.py`: Entry point for the simulation
- `simulation.py`: Core simulation logic
- `pid_controller.py`: Implementation of the Delayed PID controller
- `config.py`: Configuration handling
- `optimization.py`: PID parameter optimization
- `visualization.py`: Plotting and visualization of results
- `tests/`: Unit tests for the project components
- `config.ini`: Configuration file
- `requirements.txt`: List of project dependencies

## Running Tests

To run the unit tests:

```
python -m unittest discover tests
```

## Docker Support

A Dockerfile is provided for containerized deployment. To build and run the Docker image:

1. Build the image:
   ```
   docker build -t particle-simulation .
   ```

2. Run the container:
   ```
   docker run particle-simulation
   ```

## Contributing

Contributions to this project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

[Specify your license here, e.g., MIT License]

## Contact

[Your Name] - sumanthpv.venkateshmurthy@alumni.utoronto.ca

Project Link: [https://github.com/yourusername/particle-motion-simulation](https://github.com/yourusername/particle-motion-simulation)