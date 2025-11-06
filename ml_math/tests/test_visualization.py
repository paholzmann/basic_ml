import matplotlib # type: ignore
matplotlib.use("Agg")
import pytest # type: ignore
import numpy as np # type: ignore
from src.visualization import Visualization

# pip install pytest-mock

class TestVisualization:
    @pytest.fixture(autouse=True)
    def setup(self):
        """
        
        """
        self.visualization = Visualization()
        self.input_data = [
            np.linspace(-100, 100, 1000),
            np.linspace(-1, 1, 1000)
        ]
    @pytest.mark.parametrize("func_name", [
        "linear",
        "binary_step",
        "sigmoid",
        "tanh",
        "hard_sigmoid",
        "hard_tanh",
        "relu",
        "leaky_relu",
        "parametric_relu",
        "randomized_relu",
        "elu",
        "selu",
        "gelu",
        "swish",
        "mish",
        "softplus",
        "softmax",
        "log_softmax",
        "softsign",
        "sin",
        "cos",
        "arctan",
        "bent_identity",
        "gaussian",
        "rbf"])
    def test_visualize_one_activation(self, func_name, mocker):
        """
        
        """
        mocker.patch("matplotlib.pyplot.show")
        for x in self.input_data:
            self.visualization.visualize_one_activation(x=x, func_name=func_name)

    @pytest.mark.parametrize("func_name_arr", [
        ["linear", "binary_step", "elu"],
        ["sigmoid", "tanh", "hard_sigmoid", "hard_tanh"],
        ["relu", "leaky_relu", "parametric_relu", "randomized_relu", "elu", "selu", "gelu", "swish", "mish", "softplus"],
        ["softmax", "log_softmax"],
        ["softsign", "sin", "cos", "arctan", "bent_identity", "gaussian", "rbf"]
    ])
    
    def test_visualize_family(self, func_name_arr, mocker):
        """
        
        """
        mocker.patch("matplotlib.pyplot.show")
        for x in self.input_data:
            self.visualization.visualize_family(x=x, func_name_arr=func_name_arr)
