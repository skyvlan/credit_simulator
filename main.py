from src.controller.controller import LoanController
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    #if has sys.argv[1] then run from file
    if len(sys.argv) > 1:
        loan_controller = LoanController()
        loan_controller.run_calculation_from_file(sys.argv[1])
    else:
        loan_controller = LoanController()
        loan_controller.run_menu()

if __name__ == "__main__":
    main()

