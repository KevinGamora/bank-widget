import pytest
from unittest.mock import patch, Mock
from src.external_api import convert_to_rub, get_exchange_rate


@pytest.fixture
def transaction_usd():
    return {"amount": 100, "currency": "USD"}


@pytest.fixture
def transaction_rub():
    return {"amount": 100, "currency": "RUB"}


def test_convert_to_rub(transaction_rub):
    amount = transaction_rub["amount"]
    currency = transaction_rub["currency"]
    assert convert_to_rub(amount, currency) == 100


@patch('src.external_api.get_exchange_rate')
def test_convert_to_rub_usd(mock_get_exchange_rate, transaction_usd):
    mock_get_exchange_rate.return_value = 75.0  # mock the exchange rate

    amount = transaction_usd["amount"]
    currency = transaction_usd["currency"]
    result = convert_to_rub(amount, currency)

    assert result == 7500.0
    mock_get_exchange_rate.assert_called_once_with(currency)


@patch('src.external_api.requests.get')
def test_get_exchange_rate(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 75.0}}
    mock_get.return_value = mock_response

    with patch('os.getenv', return_value='fake_api_key'):
        rate = get_exchange_rate("USD")

    assert rate == 75.0
    mock_get.assert_called_once()
