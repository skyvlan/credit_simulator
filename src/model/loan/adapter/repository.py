from src.model.loan.domain.entity import Loan, Vehicle
from src.model.loan.domain.interface import LoanAbstractRepo, LoanAbstractUnitOfWork
class LoanRepository(LoanAbstractRepo):

    def __init__(self):
        self.loan_entity = []
        self.vehicle_entity = []

    def get_loan(self):
        return self.loan_entity

    def add_loan(self, loan: Loan):
        self.loan_entity = loan
        print(self.loan_entity)

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicle_entity = vehicle
        print(self.vehicle_entity)

    def get_vehicle(self):
        return self.vehicle_entity


