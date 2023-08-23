from src.model.loan.domain.entity import Loan, Vehicle, LoanOutput
from src.model.loan.adapter.uow import LoanUnitOfWork
from typing import List
import math
class LoanService:
    def __init__(self, uow: LoanUnitOfWork):
        self.loan = uow.loan.get_loan()
        self.vehicle = uow.loan.get_vehicle()
        self.base_interest_car_rate = 0.08
        self.base_interest_motor_rate = 0.09

    def calculate_loan(self) -> List[LoanOutput]:
        if self.vehicle.vehicle_type == "mobil":
            interest_rate = self.base_interest_car_rate
        else:
            interest_rate = self.base_interest_motor_rate
        base_loan = self.loan.total_loan - self.loan.down_payment
        yearly_installment = 0
        loan = 0
        for i in range(0, self.loan.tenor):
            if i == 0:
                loan = base_loan + (base_loan * interest_rate)
                yearly_installment = loan / self.loan.tenor
                monthly_installment = yearly_installment / 12
                yield LoanOutput(year=i+1, installment=monthly_installment, interest=interest_rate * 100)
            else:
                if i % 2 == 0:
                    interest_rate += 0.005
                else:
                    interest_rate += 0.001
                remaining_loan = loan - yearly_installment
                loan = remaining_loan + (remaining_loan * interest_rate)
                yearly_installment = loan / (self.loan.tenor - i)
                monthly_installment = yearly_installment / 12
                yield LoanOutput(year=i+1, installment=monthly_installment, interest=interest_rate * 100)

















