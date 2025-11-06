import pytest # type: ignore
from src.basic_calculator import BasicCalculator

# python -m pytest

class TestCalculator:
    @classmethod
    def setup_class(cls):
        """
        
        """
        cls.basic_calculator = BasicCalculator()
        cls.input_data = [
            (1, 2),
            (-1, 2),
            (-1, -2)
        ]
        cls.input_data_invalid = [
            ("Invalid", 1),
            ([1, 2], 3)
        ]
        cls.ref_funcs = {
            "add": lambda x, y: x + y,
            "subtract": lambda x, y: x - y,
            "divide": lambda x, y: x / y,
            "multiply": lambda x, y: x * y,
            "exponential": lambda x, y: x ** y
        }
    # -------------------------------------------------- ADD --------------------------------------------------
    @pytest.mark.parametrize("func_name", [
        "add",
        "subtract",
        "subtract",
        "divide",
        "multiply",
        "exponential"
    ])
    def test_basic_calculator_outputs(self, func_name):
        """
        
        """
        func = getattr(self.basic_calculator, func_name)
        ref_func = self.ref_funcs[func_name]
        for arr in self.input_data:
            output = func(*arr)
            expected = ref_func(*arr)
            assert output == expected

    @pytest.mark.parametrize("func_name", [
        "add",
        "subtract",
        "subtract",
        "divide",
        "multiply",
        "exponential"
    ])
    def test_basic_calculator_invalids(self, func_name):
        """
        
        """
        func = getattr(self.basic_calculator, func_name)
        ref_func = self.ref_funcs[func_name]
        for arr in self.input_data_invalid:
            with pytest.raises(ValueError):
                func(*arr)
