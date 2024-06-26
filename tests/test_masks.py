import pytest
from src.masks import mask_account_number, mask_card_number


def test_mask_account_number():
    assert mask_account_number("1234567890123456") == "1234 **** **** 3456"
    assert mask_account_number("9876543210987654") == "9876 **** **** 7654"


@pytest.mark.parametrize("card_number, masked_number", [
    ("1234567812345678", "1234 **** **** 5678"),
    ("8765432187654321", "8765 **** **** 4321"),
])
def test_mask_card_number(card_number, masked_number):
    assert mask_card_number(card_number) == masked_number
