import numpy as np


class DelayedPIDController:
    def __init__(self, k_p: float, k_i: float, k_d: float, delay_steps: int, max_force: float):
        """
       Initialize the Delayed PID Controller.
        Args:
       k_p (float): Proportional gain
       k_i (float): Integral gain
       k_d (float): Derivative gain
       delay_steps (int): Number of time steps for delay
       max_force (float): Maximum allowed control force
        """
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d
        self.delay_steps = delay_steps
        self.max_force = max_force
        self.previous_error = 0
        self.integral = 0
        self.error_history = np.zeros(delay_steps)
        self.step_count = 0

    def calculate(self, current_error: float) -> np.ndarray:
        """
        Calculate the control output based on the current error
        :param current_error:
        :return:
        """
        self.step_count += 1
        self.error_history = np.roll(self.error_history, 1)
        self.error_history[0] = current_error

        if self.step_count <= self.delay_steps:
            return np.array([0])  # Return zero output during initial delay period

        delayed_error = self.error_history[-1]
        self.integral += delayed_error
        derivative = delayed_error - self.previous_error

        output = self.k_p * delayed_error + self.k_i * self.integral + self.k_d * derivative
        self.previous_error = delayed_error

        # Saturate the output
        return np.clip(output, -self.max_force, self.max_force)

