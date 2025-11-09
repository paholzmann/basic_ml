from src.user import User
from src.math.basic_calculator import BasicCalculator
from src.cli.cli import CLI
# python -m main

class Main:
    def __init__(self):
        """
        
        """
        self.basic_calculator = BasicCalculator()
        self.user = User()

    def run_main(self):
        while True:
            # Get user operation choice
            user_operation_choice = self.user.get_user_operation_choice()
            # Add
            if user_operation_choice == 1:
                a, b = self.user.get_user_numbers(operation_type="simple")
                print(self.basic_calculator.add(a, b))

if __name__ == "__main__":
    cli = CLI()
    cli.run_commands()