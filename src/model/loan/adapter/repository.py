from src.model.loan.domain.entity import Loan, Vehicle
from src.model.loan.domain.interface import LoanAbstractRepo, LoanAbstractUnitOfWork
from src.model.loan.adapter.uow import LoanUnitOfWork
class LoanRepository(LoanAbstractRepo):

    def __init__(self):
        self.loan_entity = Loan()
        self.vehicle_entity = Vehicle()

    def get_loan(self):
        return self.loan_entity

    def add_loan(self, loan: Loan):
        self.loan_entity = loan

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicle_entity = vehicle

    def get_vehicle(self):
        return self.vehicle_entity


