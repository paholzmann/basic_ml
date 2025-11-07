
class BasicCalculator:
    def __init__(self):
        """
        
        """

    # -------------------------------------------------- BASIC MATH --------------------------------------------------
    def add(self, a, b):
        """
        
        """
        try:
            return float(a) + float(b)
        except (ValueError, TypeError):
            raise ValueError("Both inputs must be numbers or numeric strings.")
        
    def subtract(self, a, b):
        """
        
        """
        try:
            return float(a) - float(b)
        except (ValueError, TypeError):
            raise ValueError("Both inputs must be numbers or numeric strings.")
    
    def divide(self, a, b):
        """
        
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        try:
            return float(a) / float(b)
        except (ValueError, TypeError):
            raise ValueError("Both inputs must be numbers or numeric strings.")
        
    def multiply(self, a, b):
        """
        
        """
        try:
            return float(a) * float(b)
        except (ValueError, TypeError):
            raise ValueError("Both inputs must be numbers or numeric strings.")
        
    def exponential(self, a, b):
        """
        
        """
        try:
            return float(a) ** float(b)
        except:
            raise ValueError("Both inputs must be numbers or numeric strings.")