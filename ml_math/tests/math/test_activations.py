import pytest # type: ignore
import numpy as np # type: ignore
from scipy.special import erf # type: ignore
from src.math.activations import Activations

# python -m pytest

class TestActivations:
    @classmethod
    def setup_class(cls):
        """
        
        """
        cls.activations = Activations()
        cls.input_data = [
            np.array([1, 2, 3]),
            np.array([-5, 0, 5]),
            np.array([-1, -2, -3])
        ]
        cls.invalid_input_data = [
            1,
            "Invalid",
            ["Invalid", 1]
        ]

        cls.ref_funcs = {
            "linear": lambda x: x,
            "binary_step": lambda x: np.where(x >= 0, 1, 0),
            "sigmoid": lambda x: 1 / (1 + np.exp(-x)),
            "tanh": lambda x: (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x)),
            "hard_sigmoid": lambda x: np.maximum(0, np.minimum(1, 0.2 * x + 0.5)),
            "hard_tanh": lambda x: np.maximum(-1, np.minimum(1, x)),
            "relu": lambda x: np.maximum(0, x),
            "leaky_relu": lambda x: np.where(x > 0, x, 0.01 * x),
            "parametric_relu": lambda x: np.where(x > 0, x, 0.01 * x),
            "randomized_relu": lambda x: np.where(x > 0, x, 0.02 * x),
            "elu": lambda x: np.where(x > 0, x, 0.01 * (np.exp(x) - 1)),
            "selu": lambda x: 1.0507009873554805 * np.where(x > 0, x, 1.6732632423543772 * (np.exp(x) - 1)),
            "gelu": lambda x: x * 0.5 * (1 + erf(x / np.sqrt(2))),
            "swish": lambda x: x * (1 / (1 + np.exp(-x))),
            "mish": lambda x: x * ((np.exp(np.log1p(np.exp(x))) - np.exp(-np.log1p(np.exp(x)))) / (np.exp(np.log1p(np.exp(x))) + np.exp(-np.log1p(np.exp(x))))),
            "softplus": lambda x: np.log1p(np.exp(x)),
            "softmax": lambda x: np.exp(x) / np.sum(np.exp(x)),
            "log_softmax": lambda x: np.log1p(np.exp(x) / np.sum(np.exp(x))),
            "softsign": lambda x: x / (1 + np.abs(x)),
            "sin": lambda x: np.sin(x),
            "cos": lambda x: np.cos(x),
            "arctan": lambda x: np.arctan(x),
            "bent_identity": lambda x: ((np.sqrt(x ** 2 + 1) - 1) / 2) + x,
            "gaussian": lambda x: np.exp(-x ** 2),
            "rbf": lambda x: np.exp(-((x - 0.0) ** 2) / (2 * 1.0 ** 2))
        }

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
        "rbf"
    ])
    def test_activation_outputs(self, func_name):
        """

        """
        func = getattr(self.activations, func_name)
        ref_func = self.ref_funcs[func_name]
        for arr in self.input_data:
            output = func(arr)
            assert isinstance(output, (list, np.ndarray))
            assert len(output) == len(arr)
            expected = ref_func(arr)
            np.testing.assert_allclose(output, expected, rtol=1e-9)

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
        "rbf"
    ])
    def test_activation_invalid(self, func_name):
        """
        
        """
        func = getattr(self.activations, func_name)
        for arr in self.invalid_input_data:
            with pytest.raises(TypeError):
                func(arr)