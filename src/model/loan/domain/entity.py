from pydantic import BaseModel
import src.model.loan.domain.enums as enums
class Vehicle(BaseModel):
    vehicle_type: enums.VehicleType
    vehicle_condition: enums.VehicleCondition
    vehicle_year: int

class Loan(BaseModel):
    total_loan: float
    tenor: int
    down_payment: float


class DataModel(Vehicle, Loan):
    pass


