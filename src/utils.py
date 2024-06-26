import json
import logging
import os
import pandas as pd
from typing import List, Dict
from datetime import datetime

# Создание папки logs, если она не существует
if not os.path.exists('logs'):
    os.makedirs('logs')

# Настройка логера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def format_amount(amount: float, currency: str) -> str:
    """
    Форматирует сумму денег с указанием валюты.

    Args:
        amount (float): Сумма денег.
        currency (str): Валюта.

    Returns:
        str: Форматированная строка с суммой и валютой.
    """
    formatted_amount = f"{amount:.2f} {currency}"
    logger.debug(f"Formatted amount: {formatted_amount}")
    return formatted_amount


def format_date(date: str) -> str:
    """
    Форматирует дату из строки в удобочитаемый формат.

    Args:
        date (str): Дата в формате строки.

    Returns:
        str: Форматированная дата.
    """
    try:
        dt = datetime.fromisoformat(date)
        formatted_date = dt.strftime("%d-%m-%Y %H:%M:%S")
        logger.debug(f"Formatted date: {formatted_date}")
        return formatted_date
    except ValueError as e:
        logger.error(f"Error formatting date: {e}")
        return ""


def read_transactions_from_json(filepath: str) -> List[Dict]:
    """
    Читает данные о финансовых транзакциях из JSON-файла.

    Args:
        filepath (str): Путь до JSON-файла.

    Returns:
        List[Dict]: Список словарей с данными о транзакциях.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.debug(f"Read {len(data)} transactions from {filepath}")
                return data
            logger.warning(f"Data in {filepath} is not a list")
            return []
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error in file {filepath}: {e}")
        return []


def read_transactions_from_csv(filepath: str) -> List[Dict]:
    """
    Читает данные о финансовых транзакциях из CSV-файла.

    Args:
        filepath (str): Путь до CSV-файла.

    Returns:
        List[Dict]: Список словарей с данными о транзакциях.
    """
    try:
        data = pd.read_csv(filepath)
        transactions = data.to_dict(orient='records')
        logger.debug(f"Read {len(transactions)} transactions from {filepath}")
        return transactions
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        return []
    except pd.errors.EmptyDataError as e:
        logger.error(f"Empty CSV error in file {filepath}: {e}")
        return []
    except pd.errors.ParserError as e:
        logger.error(f"CSV parse error in file {filepath}: {e}")
        return []


def read_transactions_from_xlsx(filepath: str) -> List[Dict]:
    """
    Читает данные о финансовых транзакциях из XLSX-файла.

    Args:
        filepath (str): Путь до XLSX-файла.

    Returns:
        List[Dict]: Список словарей с данными о транзакциях.
    """
    try:
        data = pd.read_excel(filepath)
        transactions = data.to_dict(orient='records')
        logger.debug(f"Read {len(transactions)} transactions from {filepath}")
        return transactions
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        return []
    except ValueError as e:
        logger.error(f"Excel read error in file {filepath}: {e}")
        return []
