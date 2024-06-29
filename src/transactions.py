"""
Модуль для чтения и обработки данных о финансовых транзакциях.
"""

import re
from typing import Dict, List

import pandas as pd


def read_transactions_from_csv(filepath: str) -> List[Dict]:
    """
    Читает данные о финансовых транзакциях из CSV-файла.

    Args:
        filepath (str): Путь до CSV-файла.

    Returns:
        List[Dict]: Список словарей с данными о транзакциях.
    """
    try:
        df = pd.read_csv(filepath)
        transactions = df.to_dict('records')
        return transactions
    except FileNotFoundError:
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
        df = pd.read_excel(filepath)
        transactions = df.to_dict('records')
        return transactions
    except FileNotFoundError:
        return []


def search_transactions(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Ищет транзакции, содержащие определенную строку в описании.

    Args:
        transactions (List[Dict]): Список транзакций.
        search_string (str): Строка для поиска.

    Returns:
        List[Dict]: Список транзакций, содержащих строку в описании.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    filtered_transactions = [tx for tx in transactions if pattern.search(tx.get('description', ''))]
    return filtered_transactions


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Считает количество транзакций по категориям.

    Args:
        transactions (List[Dict]): Список транзакций.
        categories (List[str]): Список категорий.

    Returns:
        Dict[str, int]: Словарь с количеством транзакций по категориям.
    """
    category_counts = {category: 0 for category in categories}
    for tx in transactions:
        description = tx.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1
                break
    return category_counts
