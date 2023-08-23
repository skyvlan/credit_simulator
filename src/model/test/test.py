from src.model.loan.service.loan import LoanService, LoanInputService
from src.model.loan.domain.entity import Loan, Vehicle, LoanOutput
from src.model.loan.adapter.uow import LoanUnitOfWork

uow = LoanUnitOfWork()
loan_input_service = LoanInputService(uow=uow)
loan_input_service.input_loan(total_loan=100000000, tenor=12, down_payment=20000000)
loan_input_service.input_vehicle(vehicle_type="mobil", vehicle_condition="baru", vehicle_year=2021)
loan_service = LoanService(uow=uow)

loan_output = loan_service.calculate_loan()
for i in loan_output:
    print(i)

