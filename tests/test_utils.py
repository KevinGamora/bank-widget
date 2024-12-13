import pytest
from src.utils import format_amount, format_date

@pytest.mark.parametrize("amount, currency, expected", [
    (1234.56, "USD", "1234.56 USD"),
    (0, "USD", "0.00 USD"),
    (1000000, "USD", "1000000.00 USD"),
    (1234.56, "EUR", "1234.56 EUR"),
    (1234.56, "RUB", "1234.56 RUB"),
])
def test_format_amount(amount, currency, expected):
    assert format_amount(amount, currency) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2023-06-01T12:00:00", "01-06-2023 12:00:00"),
    ("2024-01-01T00:00:00", "01-01-2024 00:00:00"),
])
def test_format_date(date_str, expected):
    assert format_date(date_str) == expected
