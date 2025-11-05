import pytest # type: ignore
from src.basic_calculator import BasicCalculator

# python -m pytest

class TestCalculator:

    # -------------------------------------------------- ADD --------------------------------------------------
    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 2),
        (-1, 1, 0),
        (0, 0, 0)
    ])
    def test_add(self, a, b, expected):
        """
        
        """
        assert BasicCalculator().add(a, b) == expected

    @pytest.mark.parametrize("a,b", [
        ("Hello", 3),
        ([1, 2], 5)
    ])
    def test_add_invalid(self, a, b):
        """
        
        """
        with pytest.raises(ValueError):
            BasicCalculator().add(a, b)

    # -------------------------------------------------- SUBTRACT --------------------------------------------------
    @pytest.mark.parametrize("a,b,expected", [
        (2, 1, 1),
        (-1, -1, 0),
        (0, 0, 0)
    ])
    def test_subtract(self, a, b, expected):
        """
        
        """
        assert BasicCalculator().subtract(a, b) == expected

    @pytest.mark.parametrize("a,b", [
        ("Hello", 1),
        ([1, 2], 5)
    ])
    def test_subtract_invalid(self, a, b):
        """
        
        """
        with pytest.raises(ValueError):
            BasicCalculator().subtract(a, b)

    # -------------------------------------------------- DIVIDE --------------------------------------------------
    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 1),
        (5, 1, 5),
        (0, 1, 0)
    ])
    def test_divide(self, a, b, expected):
        """
        
        """
        assert BasicCalculator().divide(a, b) == expected

    @pytest.mark.parametrize("a,b", [
        ("Hello", 1),
        (1, 0),
        ([1, 2], 1)
    ])
    def test_divide_invalid(self, a, b):
        """
        
        """
        with pytest.raises(ValueError):
            BasicCalculator().divide(a, b)

    # -------------------------------------------------- MULTIPLY --------------------------------------------------

    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 1),
        (-5, 2, -10),
        (-2, -2, 4)
    ])
    def test_multiply(self, a, b, expected):
        """
        
        """
        assert BasicCalculator().multiply(a, b) == expected
    
    @pytest.mark.parametrize("a,b", [
        ("Hello", 1),
        ([1, 2], 1)
    ])
    def test_multiply_invalid(self, a, b):
        """
        
        """
        with pytest.raises(ValueError):
            BasicCalculator().divide(a, b)

    # -------------------------------------------------- EXPONENTIAL --------------------------------------------------
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 8),
        (-2, 3, -8),
        (-2, -3, -0.125)
    ])
    def test_exponential(self, a, b, expected):
        """
        
        """
        assert BasicCalculator().exponential(a, b) == expected

    @pytest.mark.parametrize("a,b", [
        ("Hello", 1),
        ([1, 2], 1)
    ])
    def test_exponential_invalid(self, a, b):
        """
        
        """
        with pytest.raises(ValueError):
            BasicCalculator().exponential(a, b)