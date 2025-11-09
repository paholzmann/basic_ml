import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
import matplotlib.gridspec as gridspec # type: ignore
from ..math.loss import Loss

# python -m src.visualization.loss_visualization

class LossVisualization:
    def __init__(self):
        """
        
        """
        self.loss = Loss()

    def visualize_one_loss(self, i, t, func_name):
        """
        
        """
        if not hasattr(self.loss, func_name):
            raise ValueError(f"Unknown activation function: {func_name}")
        func = getattr(self.loss, func_name)
        y = func(i, t)     
        plt.figure(figsize=(8, 5))
        plt.plot(i, y, label=func_name)
        plt.title(f"{func_name} function")
        plt.xlabel("x")
        plt.ylabel(f"{func_name}(x)")
        plt.grid(True)
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        plt.legend()
        plt.show()
        plt.close()

i = np.linspace(-10, 10, 1000)
t = np.random.uniform(-10, 10, 1000)
LossVisualization().visualize_one_loss(i=i, t=t, func_name="mse")