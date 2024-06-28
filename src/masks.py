# masks.py
import logging
import re
from pathlib import Path

# Убедитесь, что директория для логов существует
log_dir = Path('logs')
log_dir.mkdir(parents=True, exist_ok=True)

# Формирование пути к файлу логов
log_file = log_dir / 'masks.log'

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Настройка обработчика файлового логгера
file_handler = logging.FileHandler(log_file, mode='w')
file_handler.setLevel(logging.DEBUG)

# Настройка форматтера и добавление его к обработчику
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)

def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер банковского счета, заменяя средние цифры на звездочки.

    Args:
        account_number (str): Номер банковского счета.

    Returns:
        str: Маскированный номер банковского счета.
    """
    masked_number = re.sub(r"(?<=\d{4})\d(?=\d{4})", "*", account_number)
    masked_number = " ".join([masked_number[i:i + 4] for i in range(0, len(masked_number), 4)])
    logger.debug(f"Маскированный номер счета: {masked_number}")
    return masked_number

def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, заменяя средние цифры на звездочки.

    Args:
        card_number (str): Номер банковской карты.

    Returns:
        str: Маскированный номер банковской карты.
    """
    masked_number = re.sub(r"(?<=\d{4})\d(?=\d{4})", "*", card_number)
    masked_number = " ".join([masked_number[i:i + 4] for i in range(0, len(masked_number), 4)])
    logger.debug(f"Маскированный номер карты: {masked_number}")
    return masked_number
