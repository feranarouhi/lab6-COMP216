import random
import matplotlib.pyplot as plt

class DataGenerator:
    def __init__(self, base=0, delta=1, scale=1, amplitude=1, frequency=1):
        self.base = base
        self.delta = delta
        self.scale = scale
        self.amplitude = amplitude
        self.frequency = frequency

    def _normalized_value(self):
        return random.random()

    @property
    def generate_data(self):
        normalized_value = self._normalized_value()
        value = self.base + self.scale * normalized_value
        return value

    def plot_data(self, num_points=500):
        data_points = [self.generate_data for _ in range(num_points)]
        plt.plot(data_points)
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Generated Data')
        plt.show()

# Example usage:
if __name__ == "__main__":
    generator = DataGenerator(base=10, scale=5)
    generator.plot_data()
