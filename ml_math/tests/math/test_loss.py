import pytest # type: ignore
import numpy as np # type: ignore
from src.math.loss import Loss

class TestLoss:
    @classmethod
    def setup_class(cls):
        """
        
        """
        cls.loss = Loss()
        cls.input_data = [
            np.array([0.1, 0.2, 0.3]),
            np.array([-0.1, 0.0, 0.1]),
            np.array([-0.1, -0.2, -0.3])   
        ]
        cls.target_data = [
            np.array([0.9, 0.4, 0.7]),
            np.array([-0.9, 0.5, 0.9]),
            np.array([-0.9, -0.4, -0.7])
        ]
        cls.invalid_input_data = [
            1,
            "Invalid",
            ["Invalid", 1]
        ]
        cls.invalid_target_data = [
            2,
            "Invalid as well",
            ["Invalid as well", 2]
        ]
        cls.ref_funcs = {
            "mse": lambda i, t: np.mean((t - i) ** 2),
            "rmse": lambda i, t: np.sqrt(np.mean((t - i) ** 2)),
            "mae": lambda i, t: np.mean(np.abs(t - i)),
            "huber": lambda i, t: np.where(np.abs(t - i) <= 1.0, 0.5 * ((t - i) ** 2), 1.0 * (np.abs(t - i) - 0.5 * 1.0)),
            "log_cosh": lambda i, t: (i - t) + np.log1p(np.exp(-2 * (i - t))) - np.log(2),
            "binary_cross_entropy": lambda i, t: - (t * np.log(np.clip(i, 1e-9, 1-1e-9)) + (1 - t) * np.log(1 - np.clip(i, 1e-9, 1-1e-9)))
        }

    @pytest.mark.parametrize("func_name", [
        "mse",
        "rmse",
        "mae",
        "huber",
        "log_cosh",
        "binary_cross_entropy"
    ])
    def test_loss_outputs(self, func_name):
        """
        
        """
        func = getattr(self.loss, func_name)
        ref_func = self.ref_funcs[func_name]
        for i, t in zip(self.input_data, self.target_data):
            output = func(i, t)
            expected = ref_func(i, t)
            np.testing.assert_allclose(output, expected, rtol=1e-9)

    @pytest.mark.parametrize("func_name", [
        "mse",
        "rmse",
        "mae",
        "huber",
        "log_cosh",
        "binary_cross_entropy"
    ])
    def test_loss_invalid(self, func_name):
        """
        
        """
        func = getattr(self.loss, func_name)
        for i, t in zip(self.invalid_input_data, self.invalid_target_data):
            with pytest.raises(TypeError):
                func(i, t)