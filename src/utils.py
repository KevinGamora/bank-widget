"""
Модуль для работы с банковскими транзакциями из различных источников.
"""

import json
import logging
import os
import re
from datetime import datetime
from typing import Dict, List

import pandas as pd

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


def search_transactions(transactions: List[Dict], search_term: str) -> List[Dict]:
    """
    Ищет транзакции по строке поиска в описании.

    Args:
        transactions (List[Dict]): Список транзакций.
        search_term (str): Строка поиска.

    Returns:
        List[Dict]: Список транзакций, содержащих строку поиска в описании.
    """
    regex = re.compile(re.escape(search_term), re.IGNORECASE)
    result = [transaction for transaction in transactions if regex.search(transaction.get('description', ''))]
    logger.debug(f"Found {len(result)} transactions matching search term '{search_term}'")
    return result


def categorize_transactions(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по категориям.

    Args:
        transactions (List[Dict]): Список транзакций.
        categories (List[str]): Список категорий.

    Returns:
        Dict[str, int]: Словарь с категориями и количеством транзакций в каждой категории.
    """
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
    logger.debug(f"Transaction counts by category: {category_count}")
    return category_count


def main():
    """
    Основная функция для работы с пользователем и выполнения различных операций с транзакциями.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input("Ваш выбор: ")
        if choice in ['1', '2', '3']:
            break
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

    file_path = input("Введите путь к файлу с транзакциями: ")

    if choice == '1':
        transactions = read_transactions_from_json(file_path)
        file_type = 'JSON'
    elif choice == '2':
        transactions = read_transactions_from_csv(file_path)
        file_type = 'CSV'
    else:
        transactions = read_transactions_from_xlsx(file_path)
        file_type = 'XLSX'

    if not transactions:
        print(f"Не удалось загрузить транзакции из {file_type}-файла.")
        return

    print(f"Для обработки выбран {file_type}-файл.")

    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").upper()
        if status in statuses:
            break
        print(f"Статус операции '{status}' недоступен.")

    filtered_transactions = [t for t in transactions if t.get('status', '').upper() == status]
    print(f"Операции отфильтрованы по статусу '{status}'.")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == 'да':
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = sort_order == 'по убыванию'
        filtered_transactions.sort(key=lambda x: x.get('date', ''), reverse=reverse)

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_choice == 'да':
        filtered_transactions = [t for t in filtered_transactions if t.get('currency', '').upper() == 'RUB']

    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if search_choice == 'да':
        search_term = input("Введите слово для поиска в описании: ").strip()
        filtered_transactions = search_transactions(filtered_transactions, search_term)

    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for t in filtered_transactions:
            date = format_date(t.get('date', ''))
            description = t.get('description', '')
            account = t.get('account', '')
            amount = format_amount(t.get('amount', 0.0), t.get('currency', ''))
            print(f"\nДата: {date}\nОписание: {description}\nСчет: {account}\nСумма: {amount}")
    else:
        print("Нет операций, соответствующих критериям фильтрации.")

    logger.info("Программа завершена.")


if __name__ == "__main__":
    main()
