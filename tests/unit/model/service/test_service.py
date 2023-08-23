from unittest.mock import Mock

import pytest

from src.model.loan.adapter.uow import LoanUnitOfWork
from src.model.loan.domain.entity import Loan, Vehicle
from src.model.loan.service.loan import LoanInputService, LoanService


@pytest.fixture
def mock_uow():
    return Mock(spec=LoanUnitOfWork)


def test_calculate_loan(mock_uow):
    # Set up mock UoW
    mock_uow.loan = Mock()

    mock_uow.loan.get_loan.return_value = Loan(
        total_loan=100000, tenor=5, down_payment=25000
    )
    mock_uow.loan.get_vehicle.return_value = Vehicle(
        vehicle_type="mobil", vehicle_condition="Baru", vehicle_year=2019
    )

    # Create LoanService instance with the mock UoW
    loan_service = LoanService(mock_uow)

    # Calculate the loan and get the result
    loan_output_list = list(loan_service.calculate_loan())

    # Perform assertions on loan_output_list

    # Example assertion for the first year
    assert loan_output_list[0].year == 1
    assert math.isclose(
        loan_output_list[0].installment, 6583.333333, rel_tol=1e-6
    )
    assert math.isclose(loan_output_list[0].interest, 8.0, rel_tol=1e-6)

    # ... perform similar assertions for other years ...


def test_input_loan(mock_uow):
    # Set up mock UoW
    mock_uow.loan = Mock()

    # Create LoanInputService instance with the mock UoW
    input_service = LoanInputService(mock_uow)

    # Call the input_loan method
    input_service.input_loan(total_loan=100000, tenor=5, down_payment=25000)

    # Perform assertions on the mock UoW's add_loan method
    mock_uow.loan.add_loan.assert_called_once_with(
        Loan(total_loan=100000, tenor=5, down_payment=25000)
    )


# Write similar tests for the input_vehicle method in LoanInputService


def test_input_vehicle(mock_uow):
    # Set up mock UoW
    mock_uow.loan = Mock()

    # Create LoanInputService instance with the mock UoW
    input_service = LoanInputService(mock_uow)

    # Call the input_vehicle method
    input_service.input_vehicle(
        vehicle_type="mobil", vehicle_condition="Baru", vehicle_year=2019
    )

    # Perform assertions on the mock UoW's add_vehicle method
    mock_uow.loan.add_vehicle.assert_called_once_with(
        Vehicle(
            vehicle_type="mobil", vehicle_condition="Baru", vehicle_year=2019
        )
    )
