from src.model.loan.domain.entity import Loan, Vehicle
from src.model.loan.domain.interface import LoanAbstractUnitOfWork
from src.model.loan.adapter.repository import LoanRepository
from typing import List
class LoanUnitOfWork(LoanAbstractUnitOfWork):

    def __init__(self):
        self.loan = LoanRepository()
        self.commited = False

    def commit(self):
        if self.commited:
            raise ValueError("Transaction already commited")
        self.commited = True


    def rollback(self):
        self.commited = False
        self.loan = LoanRepository()








