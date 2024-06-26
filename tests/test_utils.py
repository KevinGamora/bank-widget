
import pytest
from src.utils import format_amount, format_date, read_transactions_from_json
import json


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


@pytest.fixture
def sample_transactions_file(tmp_path):
    data = [
        {"amount": 100.0, "currency": "USD"},
        {"amount": 200.0, "currency": "EUR"}
    ]
    file_path = tmp_path / "sample_transactions.json"
    with open(file_path, 'w') as file:
        json.dump(data, file)
    return file_path


def test_read_transactions_from_json(sample_transactions_file):
    transactions = read_transactions_from_json(sample_transactions_file)
    assert len(transactions) == 2
    assert transactions[0]['amount'] == 100.0
    assert transactions[0]['currency'] == "USD"


def test_read_transactions_from_json_empty_file(tmp_path):
    empty_file_path = tmp_path / "empty.json"
    empty_file_path.touch()
    transactions = read_transactions_from_json(empty_file_path)
    assert transactions == []


def test_read_transactions_from_json_invalid_file(tmp_path):
    invalid_file_path = tmp_path / "invalid.json"
    with open(invalid_file_path, 'w') as file:
        file.write("not a json")
    transactions = read_transactions_from_json(invalid_file_path)
    assert transactions == []
