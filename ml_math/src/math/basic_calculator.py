from src.logging.logger_config import Logger

class BasicCalculator:
    def __init__(self):
        """
        
        """
        self.log = Logger(self.__class__.__name__)

    # -------------------------------------------------- BASIC MATH --------------------------------------------------
    def add(self, a, b):
        """
        
        """
        try:
            result = float(a) + float(b)
            self.log.info(f"Add: {a} + {b} = {result}")
            return result
        except (ValueError, TypeError):
            self.log.error(f"Invalid input for add: {a}, {b}")
            raise ValueError("Both inputs must be numbers or numeric strings.")
        
    def subtract(self, a, b):
        """
        
        """
        try:
            result = float(a) - float(b)
            self.log.info(f"Subtract: {a} - {b} = {result}")
            return result
        except (ValueError, TypeError):
            self.log.error(f"Invalid input for subtract: {a}, {b}")
            raise ValueError("Both inputs must be numbers or numeric strings.")
    
    def divide(self, a, b):
        """
        
        """
        if b == 0:
            self.log.error(f"Division by zero is not allowed: {a}, {b}")
            raise ValueError("Division by zero is not allowed.")
        try:
            result = float(a) / float(b)
            self.log.info(f"Divide: {a} / {b} = {result}")
            return result
        except (ValueError, TypeError):
            self.log.error(f"Invalid input for divide: {a}, {b}")
            raise ValueError("Both inputs must be numbers or numeric strings.")
        
    def multiply(self, a, b):
        """
        
        """
        try:
            result = float(a) * float(b)
            self.log.info(f"Multiply: {a} * {b} = {result}")
            return result
        except (ValueError, TypeError):
            self.log.error(f"Invalid input for multiply: {a}, {b}")
            raise ValueError("Both inputs must be numbers or numeric strings.")
        
    def exponential(self, a, b):
        """
        
        """
        try:
            result = float(a) ** float(b)
            self.log.info(f"Exponential: {a} ** {b} = {result}")
            return result
        except (ValueError, TypeError):
            self.log.error(f"Invalid input for exponential: {a}, {b}")
            raise ValueError("Both inputs must be numbers or numeric strings.")