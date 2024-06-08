import pytest
from src.utils import format_currency

@pytest.mark.parametrize("value, expected", [
    (1234.56, "$1,234.56"),
    (0, "$0.00"),
    (1000000, "$1,000,000.00"),
])
def test_format_currency(value, expected):
    assert format_currency(value) == expected
