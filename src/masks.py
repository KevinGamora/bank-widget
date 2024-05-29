# src/masks.py


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты. Видны первые 6 и последние 4 цифры, остальные заменены на '*'.
    Формат: XXXX XX** **** XXXX

    :param card_number: str - номееер карты
    :return: str - маскированный номер карты
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета. Видны только последние 4 цифры, остальные заменены на '*'.
    Формат: **XXXX

    :param account_number: str - номер счета
    :return: str - маскированный номер счета
    """
    return f"**{account_number[-4:]}"


# Этот блок я сделал просто для проверки себя
if __name__ == "__main__":
    # Примеры для тестирования
    card_number = "7000792289606361"
    masked_card_number = mask_card_number(card_number)
    print(masked_card_number)  # Ожидаемый вывод: 7000 79** **** 6361

    account_number = "73654108430135874305"
    masked_account_number = mask_account_number(account_number)
    print(masked_account_number)  # Ожидаемый вывод: **4305
