import logging
import os
import re

# Создание папки logs, если она не существует
if not os.path.exists('logs'):
    os.makedirs('logs')

# Настройка логера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер банковского счета, оставляя первые и последние 4 цифры видимыми.

    Args:
        account_number (str): Номер банковского счета.

    Returns:
        str: Замаскированный номер счета.
    """
    masked_number = re.sub(r"(?<=\d{4})\d(?=\d{4})", "*", account_number)
    masked_number = " ".join([masked_number[i : i + 4] for i in range(0, len(masked_number), 4)])
    logger.debug(f"Masked account number: {masked_number}")
    return masked_number


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, оставляя первые и последние 4 цифры видимыми.

    Args:
        card_number (str): Номер банковской карты.

    Returns:
        str: Замаскированный номер карты.
    """
    masked_number = f"{card_number[:4]} {'*' * 4} {'*' * 4} {card_number[-4:]}"
    logger.debug(f"Masked card number: {masked_number}")
    return masked_number
