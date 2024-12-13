import pytest
from src.masks import mask_card_number

@pytest.mark.parametrize("card_number, masked_number", [
    ("1234567812345678", "1234 **** **** 5678"),
    ("8765432187654321", "8765 **** **** 4321"),
])
def test_mask_card_number(card_number, masked_number):
    assert mask_card_number(card_number) == masked_number


@pytest.mark.parametrize("card_number, masked_number", [
    ("1234567812345678", "1234 **** **** 5678"),
    ("8765432187654321", "8765 **** **** 4321"),
])
def test_mask_card_number(card_number, masked_number):
    assert mask_card_number(card_number) == masked_number
