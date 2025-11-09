import matplotlib.pyplot as plt # type: ignore
import matplotlib.gridspec as gridspec # type: ignore
import numpy as np # type: ignore
from ..math.activations import Activations

# python -m src.visualization

class ActivationVisualization:
    def __init__(self):
        """
        
        """
        self.activations = Activations()
    # -------------------------------------------------- UTILITIES --------------------------------------------------
    def visualize_one_activation(self, x, func_name):
        """
        
        """
        if not hasattr(self.activations, func_name):
            raise ValueError(f"Unknown activation function: {func_name}")
        func = getattr(self.activations, func_name)
        y = func(x)
        plt.figure(figsize=(8, 5))
        plt.plot(x, y, label=func_name)
        plt.title(f"{func_name} function")
        plt.xlabel("x")
        plt.ylabel(f"{func_name}(x)")
        plt.grid(True)
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        plt.legend()
        plt.show()
        plt.close()      
 
    def visualize_family(self, x, func_name_arr):
        """
        
        """
        num_plots = len(func_name_arr)
        fig = plt.figure(figsize=(8, 4 * ((num_plots + 1) // 2)))
        gs = gridspec.GridSpec((num_plots + 1) // 2, 2, figure=fig)

        for i, func_name in enumerate(func_name_arr):
            if not hasattr(self.activations, func_name):
                raise ValueError(f"Unknown activation function: {func_name}")
            func = getattr(self.activations, func_name)
            y = func(x)
            if num_plots % 2 == 1 and i == num_plots - 1:
                ax = fig.add_subplot(gs[i // 2, :])
            else:
                ax = fig.add_subplot(gs[i // 2, i % 2])

            ax.plot(x, y, label=func_name)
            ax.set_title(func_name)
            ax.set_xlabel("x")
            ax.set_ylabel(f"{func_name}(x)")
            ax.grid(True)
            ax.axhline(0, color="black", linewidth=0.5)
            ax.axvline(0, color="black", linewidth=0.5)
            ax.legend()
        plt.tight_layout()
        plt.show()