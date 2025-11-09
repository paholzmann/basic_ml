import argparse
from ..math.basic_calculator import BasicCalculator

# python -m main basic_calculator add 3 1

class CLI:
    def __init__(self):
        """
        
        """
        self.basic_calculator = BasicCalculator()
        self.parser = argparse.ArgumentParser(description="Test")
        self.subparser = self.parser.add_subparsers(dest="command")
        self.setup_basic_calculator_commands()

    def setup_basic_calculator_commands(self):
        """
        
        """
        basic_calculator_parser = self.subparser.add_parser(
            "basic_calculator",
            help="Basic mathematical functions"
            )
        basic_calculator_parser.add_argument(
            "operation", choices=["add", "subtract", "divide", "multiply", "exponential"],
            help="Choose the desired operation"
            )
        basic_calculator_parser.add_argument("a", type=float, help="First value")
        basic_calculator_parser.add_argument("b", type=float, help="Second value")

    def run_commands(self):
        """
        
        """
        args = self.parser.parse_args()
        if args.command == "basic_calculator":
            if args.operation == "add":
                result = self.basic_calculator.add(args.a, args.b)
            elif args.operation == "subtract":
                result = self.basic_calculator.subtract(args.a, args.b)
            elif args.operation == "divide":
                result = self.basic_calculator.divide(args.a, args.b)
            elif args.operation == "multiply":
                result = self.basic_calculator.multiply(args.a, args.b)
            elif args.operation == "exponential":
                result = self.basic_calculator.exponential(args.a, args.b)
            print(result)
