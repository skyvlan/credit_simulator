from pydantic import BaseModel
import src.model.loan.domain.enums as enums
from typing import Optional
class Vehicle(BaseModel):
    vehicle_type: enums.VehicleType
    vehicle_condition: enums.VehicleCondition
    vehicle_year: int

class Loan(BaseModel):
    total_loan: float
    tenor: int
    down_payment: float


class LoanOutput(BaseModel):
    year: int
    installment: float
    interest: float





