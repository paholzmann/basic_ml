import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
from .activations import Activations

# python -m src.visualization

class Visualization:
    def __init__(self):
        """
        
        """
        self.activations = Activations()

    def visualize_one_line(self, x, y, func_name):
        """
        
        """
        plt.figure(figsize=(8, 5))
        plt.plot(x, y, label=func_name, color="blue")
        plt.title(f"{func_name} function")
        plt.xlabel("x")
        plt.ylabel(f"{func_name}(x)")
        plt.grid(True)
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        plt.legend()
        plt.show()      
    # -------------------------------------------------- LINEAR & CLASSIC ACTIVATIONS --------------------------------------------------
    def visualize_linear(self, x):
        """
        
        """
        y = self.activations.linear(x=x)
        self.visualize_one_line(x=x, y=y, func_name="Linear")

    def visualize_binary_step(self, x):
        """
        
        """
        y = self.activations.binary_step(x=x)
        self.visualize_one_line(x=x, y=y, func_name="Binary step")
    
    # -------------------------------------------------- SIGMOID FAMILY --------------------------------------------------
    def visualize_sigmoid(self, x):
        """
        Visualisiert die Sigmoid-Aktivierungsfunktion.
        """
        y = self.activations.sigmoid(x=x)
        self.visualize_one_line(x=x, y=y, func_name="Sigmoid")

    

        
x = np.linspace(-10, 10, 1000)
Visualization().visualize_linear(x=x)
Visualization().visualize_binary_step(x=x)
Visualization().visualize_sigmoid(x=x)