import configparser


class SimulationConfig:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        # Time steps for simulation
        self.dt = self.config.getfloat("Simulation", "dt")
        self.T = self.config.getint("Simulation", "T")
        self.delay_time = self.config.getfloat("Simulation", "delay_time")
        self.max_force = self.config.getfloat("Controller", "max_force")
        self.initial_pid_params = [
            self.config.getfloat("Controller", "initial_Kp"),
            self.config.getfloat("Controller", "initial_Ki"),
            self.config.getfloat("Controller", "initial_Kd")
        ]
        self.optimization_bounds = [
            (self.config.getfloat('Optimization', 'min_Kp'),
             self.config.getfloat('Optimization', 'max_Kp')),
            (self.config.getfloat('Optimization', 'min_Ki'),
             self.config.getfloat('Optimization', 'max_Ki')),
            (self.config.getfloat('Optimization', 'min_Kd'),
             self.config.getfloat('Optimization', 'max_Kd'))
        ]
