from unittest.mock import Mock, patch
from src.controller.controller import LoanController


def test_run_menu():

    mock_view = Mock()
    mock_view.input.side_effect = ["1", "motor", "baru", "2022", "50000000", "3", "25000000"]
    controller = LoanController()
    controller.view = mock_view


    mock_input_service = Mock()
    controller.loan_input_service = mock_input_service


    mock_loan_service = Mock()
    controller.loan_service = mock_loan_service
    mock_loan_service.calculate_loan.return_value = [{"year": 1, "installment": 1000, "interest": 8.0}]


    controller.run_menu()


    assert mock_view.output.call_count == 9  
    mock_input_service.input_vehicle.assert_called_once()
    mock_input_service.input_loan.assert_called_once()
    mock_loan_service.calculate_loan.assert_called_once()

