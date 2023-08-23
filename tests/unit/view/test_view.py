from unittest.mock import Mock, patch

import pytest

from src.model.loan.domain.entity import LoanOutput
from src.view.ConsoleView import ConsoleView


@pytest.fixture
def mock_console_view():
    return ConsoleView()


def test_input_vehicle_type_valid(mock_console_view):
    with patch("builtins.input", side_effect=["Mobil"]):
        result = mock_console_view.input_vehicle_type()

    assert result == "mobil"


def test_input_vehicle_type_invalid_then_valid(mock_console_view):
    with patch("builtins.input", side_effect=["InvalidType", "Motor"]):
        result = mock_console_view.input_vehicle_type()

    assert result == "motor"


def test_input_vehicle_condition_valid(mock_console_view):
    with patch("builtins.input", side_effect=["Baru"]):
        result = mock_console_view.input_vehicle_condition()

    assert result == "baru"


def test_input_vehicle_condition_invalid_then_valid(mock_console_view):
    with patch("builtins.input", side_effect=["InvalidCondition", "Bekas"]):
        result = mock_console_view.input_vehicle_condition()

    assert result == "bekas"


def test_input_vehicle_year_valid(mock_console_view):
    with patch("builtins.input", side_effect=["2021"]):
        result = mock_console_view.input_vehicle_year()

    assert result == 2021


def test_input_vehicle_year_invalid_then_valid(mock_console_view):
    with patch("builtins.input", side_effect=["InvalidYear", "2021"]):
        result = mock_console_view.input_vehicle_year()

    assert result == 2021


def test_input_total_loan_valid(mock_console_view):
    with patch("builtins.input", side_effect=["100000000"]):
        result = mock_console_view.input_total_loan()

    assert result == 100000000


def test_input_total_loan_invalid_then_valid(mock_console_view):
    with patch(
        "builtins.input", side_effect=["InvalidTotalLoan", "100000000"]
    ):
        result = mock_console_view.input_total_loan()

    assert result == 100000000


def test_input_tenor_valid(mock_console_view):
    with patch("builtins.input", side_effect=["6"]):
        result = mock_console_view.input_tenor()

    assert result == 6


def test_input_tenor_invalid_then_valid(mock_console_view):
    with patch("builtins.input", side_effect=["InvalidTenor", "6"]):
        result = mock_console_view.input_tenor()

    assert result == 6


def test_input_tenor_invalid_then_invalid_then_valid(mock_console_view):
    with patch(
        "builtins.input", side_effect=["InvalidTenor", "InvalidTenor", "6"]
    ):
        result = mock_console_view.input_tenor()

    assert result == 6


def test_input_down_payment_valid(mock_console_view):
    with patch("builtins.input", side_effect=["25000000"]):
        result = mock_console_view.input_down_payment()

    assert result == 25000000


def test_input_down_payment_invalid_then_valid(mock_console_view):
    with patch(
        "builtins.input", side_effect=["InvalidDownPayment", "25000000"]
    ):
        result = mock_console_view.input_down_payment()

    assert result == 25000000
