from abc import ABC, abstractmethod
from src.model.loan.domain.entity import Loan, Vehicle

class LoanAbstractRepo(ABC):
    def __init__(self, db):
        self.db = db

    def get_loan(self):
        raise NotImplementedError

    def add_loan(self, loan: Loan):
        raise NotImplementedError

    def add_vehicle(self, vehicle: Vehicle):
        raise NotImplementedError

    def get_vehicle(self):
        raise NotImplementedError

class LoanAbstractUnitOfWork(ABC):
    loan: LoanAbstractRepo

    def __enter__(self) -> "LoanAbstractUnitOfWork":
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError



