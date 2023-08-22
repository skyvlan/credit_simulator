from src.model.loan.domain.entity import Loan, Vehicle
from src.model.loan.domain.interface import LoanAbstractRepo, LoanAbstractUnitOfWork
from typing import List
class LoanUnitOfWork(LoanAbstractUnitOfWork):

    def __init__(self, session):
        self.entity = []
        self.commited = False

    def commit(self):
        if self.commited:
            raise ValueError("Transaction already commited")





