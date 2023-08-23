from src.model.loan.domain.entity import Loan, Vehicle
from src.model.loan.domain.interface import LoanAbstractRepo, LoanAbstractUnitOfWork
class LoanRepository(LoanAbstractRepo):

    def __init__(self):
        self.loan_entity = None
        self.vehicle_entity = None

    def get_loan(self):
        return self.loan_entity

    def add_loan(self, loan: Loan):
        self.loan_entity = loan


    def add_vehicle(self, vehicle: Vehicle):
        self.vehicle_entity = vehicle


    def get_vehicle(self):
        return self.vehicle_entity


