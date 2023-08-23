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
        base_loan = self.loan.total_loan - self.loan.down_payment #100000000 - 25000000 = 75000000
        for i in range(0, self.loan.tenor):
            if i == 0:
                loan = base_loan + (base_loan * interest_rate)
                yearly_installment = loan / self.loan.tenor
                monthly_installment = yearly_installment / 12
                print("yearly=",yearly_installment)
                print("monthly=",monthly_installment)
                yield LoanOutput(year=i+1, installment=monthly_installment, interest=interest_rate * 100)
            else:
                if i % 2 == 0:
                    interest_rate += 0.005
                else:
                    interest_rate += 0.001
                remaining_loan = loan - yearly_installment
                loan = remaining_loan + (remaining_loan * interest_rate)
                print("loan=",loan)
                print("yearly=",yearly_installment)
                print("monthly=",monthly_installment)
                yearly_installment = loan / (self.loan.tenor - i)
                monthly_installment = yearly_installment / 12
                yield LoanOutput(year=i+1, installment=monthly_installment, interest=interest_rate * 100)

















