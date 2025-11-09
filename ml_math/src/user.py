from src.math.basic_calculator import BasicCalculator

class User:
    def __init__(self):
        """
        
        """
        self.basic_calculator = BasicCalculator()

    def print_user_operation_choices(self):
        """
        
        """
        print("Please choose an operation.")
        print("1. Add 2 numbers")
        print("2. Exit")

    def get_user_operation_choice(self):
        """
        
        """
        user_operation_choice = input("Choose an operation: ")
        try:
            user_operation_choice = int(user_operation_choice)
            return user_operation_choice
        except ValueError:
            print("You can only enter a number.")
            return None
        
    def get_user_numbers(self, operation_type):
        """
        simple: 2 numbers
        """
        if operation_type == "simple":
            a = input("Choose your first number: ")
            b = input("Choose your second number: ")
            try:
                a = float(a)
                b = float(b)
                return a, b
            except ValueError:
                print("You can only enter numbers.")
                return (0, 0)