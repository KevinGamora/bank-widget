def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя видимыми только первые и последние 4 цифры.

    Args:
        account_number (str): Полный номер счета.

    Returns:
        str: Замаскированный номер счета.
    """
    return f"{account_number[:4]}{'*' * (len(account_number) - 8)}{account_number[-4:]}"

def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя видимыми только первые и последние 4 цифры.
    Разделяет номер на группы по 4 цифры.

    Args:
        card_number (str): Полный номер карты.

    Returns:
        str: Замаскированный номер карты.
    """
    masked_middle = '*' * 4 + ' ' + '*' * 4
    return f"{card_number[:4]} {masked_middle} {card_number[-4:]}"
