from src.model.loan.domain.entity import Loan, Vehicle
from src.model.loan.domain.interface import LoanAbstractRepo, LoanAbstractUnitOfWork
from typing import List
class LoanUnitOfWork(LoanAbstractUnitOfWork):

    def __init__(self, session):
        self.vehicle_entity = Vehicle
        self.loan_entity = Loan
        self.commited = False

    def commit(self):
        if self.commited:
            raise ValueError("Transaction already commited")
        self.commited = True

    def rollback(self):
        self.vehicle_entity = []
        self.loan_entity = []







