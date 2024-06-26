import re


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер банковского счета, оставляя первые и последние 4 цифры видимыми.

    Args:
        account_number (str): Номер банковского счета.

    Returns:
        str: Замаскированный номер счета.
    """
    masked_number = re.sub(r"(?<=\d{4})\d(?=\d{4})", "*", account_number)
    return " ".join([masked_number[i:i + 4] for i in range(0, len(masked_number), 4)])


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, оставляя первые и последние 4 цифры видимыми.

    Args:
        card_number (str): Номер банковской карты.

    Returns:
        str: Замаскированный номер карты.
    """
    return f"{card_number[:4]} {'*' * 4} {'*' * 4} {card_number[-4:]}"
