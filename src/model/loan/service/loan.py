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


    #loan flow:
    #1.Tenor Cannot more than 6 years.
    #2 Down payment "MOBIL" >=35% and "MOTOR" >=25% total_loan
    #3. Interest year on year increase 0.5% every even year and 0.1% every odd year
    #4. Interest rate for "MOBIL" is 8% and "MOTOR" is 9%
    #5. Tenor is 1-6 years
    #6. calculate installment per month after down payment
    def calculate_loan(self) -> List[LoanOutput]:
        if self.vehicle.vehicle_type == "mobil":
            interest_rate = self.base_interest_car_rate
        else:
            interest_rate = self.base_interest_motor_rate
        loan = self.loan.total_loan - self.loan.down_payment
        for i in range(0, self.loan.tenor):
            if i > 0:
                if i % 2 == 0:
                    interest_rate += 0.005
                else:
                    interest_rate += 0.001
            interest = loan * interest_rate
            installment = (loan + interest) / (self.loan.tenor * 12)
            yield LoanOutput(year=i+1, installment=installment, interest=interest_rate * 100)

















