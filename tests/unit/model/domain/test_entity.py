import unittest

from src.model.loan.domain.entity import Loan, Vehicle, LoanOutput


class UnitTest(unittest.TestCase):

    def test_input_loan(self):
        loan = Loan(total_loan=100000000, tenor=3, down_payment=25000000)
        self.assertEqual(loan.total_loan, 100000000)
        self.assertEqual(loan.tenor, 3)
        self.assertEqual(loan.down_payment, 25000000)

    def test_input_loan_different(self):
        loan = Loan(total_loan=100000000, tenor=3, down_payment=25000000)
        self.assertNotEqual(loan.total_loan, 1000000000)
        self.assertNotEqual(loan.tenor, 4)
        self.assertNotEqual(loan.down_payment, 250000000)

    def test_input_vehicle(self):
        vehicle = Vehicle(vehicle_type="mobil", vehicle_condition="baru", vehicle_year=2021)
        self.assertEqual(vehicle.vehicle_type, "mobil")
        self.assertEqual(vehicle.vehicle_condition, "baru")
        self.assertEqual(vehicle.vehicle_year, 2021)

    def test_input_vehicle_different(self):
        vehicle = Vehicle(vehicle_type="mobil", vehicle_condition="baru", vehicle_year=2021)
        self.assertNotEqual(vehicle.vehicle_type, "motor")
        self.assertNotEqual(vehicle.vehicle_condition, "bekas")
        self.assertNotEqual(vehicle.vehicle_year, 2020)

    def test_loan_output(self):
        loan_output = LoanOutput(year=2021, installment=29166666.666666668, interest=0.05)
        self.assertEqual(loan_output.year, 2021)
        self.assertEqual(loan_output.installment, 29166666.666666668)
        self.assertEqual(loan_output.interest, 0.05)

    def test_loan_output_different(self):
        loan_output = LoanOutput(year=2021, installment=29166666.666666668, interest=0.05)
        self.assertNotEqual(loan_output.year, 2020)
        self.assertNotEqual(loan_output.installment, 23166666)
        self.assertNotEqual(loan_output.interest, 0.06)

    def test_invalid_vehicle_type(self):
        with self.assertRaises(ValueError):
            Vehicle(vehicle_type="kereta api", vehicle_condition="baru", vehicle_year=2021)

    def test_invalid_vehicle_type(self):
        with self.assertRaises(ValueError):
            Vehicle(vehicle_type="mobil", vehicle_condition="kuno", vehicle_year=2021)