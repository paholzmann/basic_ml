import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class ModelVisualization:
    def __init__(self):
        """
        
        """

    def visualize_predictions(self, y_pred, y):
        """
        
        """
        plt.figure(figsize=(12, 6))
        plt.plot(y, label="Actual close values", color="blue")
        plt.plot(y_pred, label="Predicted close values", color="red", linestyle="--")
        plt.title("Actual vs predicted close values")
        plt.xlabel("Timestamp")
        plt.ylabel("Close")
        plt.legend()
        plt.show()

    def visualize_loss(self, loss_arr, loss_name):
        """
        
        """
        plt.figure(figsize=(12, 6))
        plt.plot(loss_arr, label=f"{loss_name}", color="blue")
        plt.title(f"{loss_name}")
        plt.xlabel("Epoch")
        plt.ylabel(f"{loss_name}")
        plt.legend()
        plt.show()