from src.user import User
from src.basic_calculator import BasicCalculator

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
    main = Main()
    main.run_main()