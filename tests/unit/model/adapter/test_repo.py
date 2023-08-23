import unittest
from src.model.loan.adapter.repository import LoanRepository
from src.model.loan.adapter.uow import LoanUnitOfWork
from src.model.loan.domain.entity import Loan, Vehicle

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.uow = LoanUnitOfWork()
        self.loan_repo = LoanRepository()

    def test_input_loan(self):
        loan = Loan(total_loan=100000000, tenor=3, down_payment=25000000)
        self.loan_repo.add_loan(loan=loan)
        self.uow.loan = self.loan_repo
        self.assertEqual(self.uow.loan.get_loan(), loan)

    def test_input_vehicle(self):
        vehicle = Vehicle(vehicle_type="mobil", vehicle_condition="baru", vehicle_year=2021)
        self.loan_repo.add_vehicle(vehicle=vehicle)
        self.uow.loan = self.loan_repo
        self.assertEqual(self.uow.loan.get_vehicle(), vehicle)

    def test_input_loan_fail(self):
        loan = Loan(total_loan=100000000, tenor=3, down_payment=15000000)
        self.loan_repo.add_loan(loan=loan)
        self.uow.loan = self.loan_repo
        self.assertNotEqual(self.uow.loan.get_loan(), Loan(total_loan=100000000, tenor=3, down_payment=25000000))

    def test_input_vehicle_fail(self):
        vehicle = Vehicle(vehicle_type="mobil", vehicle_condition="baru", vehicle_year=2021)
        self.loan_repo.add_vehicle(vehicle=vehicle)
        self.uow.loan = self.loan_repo
        self.assertNotEqual(self.uow.loan.get_vehicle(), Vehicle(vehicle_type="motor", vehicle_condition="baru", vehicle_year=2021))

