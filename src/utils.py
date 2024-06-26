import json
from typing import List, Dict


def format_amount(amount: float, currency: str) -> str:
    """
    Форматирует сумму денег с указанием валюты.

    Args:
        amount (float): Сумма денег.
        currency (str): Валюта.

    Returns:
        str: Форматированная строка с суммой и валютой.
    """
    return f"{amount:.2f} {currency}"


def format_date(date: str) -> str:
    """
    Форматирует дату из строки в удобочитаемый формат.

    Args:
        date (str): Дата в формате строки.

    Returns:
        str: Форматированная дата.
    """
    from datetime import datetime
    dt = datetime.fromisoformat(date)
    return dt.strftime("%d-%m-%Y %H:%M:%S")


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
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
