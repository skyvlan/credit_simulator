from src.model.loan.domain.entity import Loan, Vehicle
from src.model.loan.domain.interface import LoanAbstractRepo, LoanAbstractUnitOfWork
from src.model.loan.adapter.uow import LoanUnitOfWork
class LoanRepository(LoanAbstractRepo):

    def __init__(self):
        self.uow = LoanUnitOfWork()

    def get_loan(self):
        return self.uow.loan_entity

    def add_loan(self, loan: Loan):
        self.uow.loan_entity = loan

    def add_vehicle(self, vehicle: Vehicle):
        self.uow.vehicle_entity = vehicle

    def get_vehicle(self):
        return self.uow.vehicle_entity


