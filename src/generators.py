# src/generators.py

from typing import Dict, Iterator, List, Union


def filter_by_currency(transactions: Union[List[Dict], Iterator[Dict]], currency_code: str) -> Iterator[Dict]:
    """
    Возвращает итератор по операциям с указанной валютой.

    Args:
        transactions (Union[List[Dict], Iterator[Dict]]): Список или итератор операций.
        currency_code (str): Код валюты (например, "USD").

    Yields:
        Iterator[Dict]: Итератор по операциям с указанной валютой.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: Union[List[Dict], Iterator[Dict]]) -> Iterator[str]:
    """
    Возвращает итератор по описаниям операций.

    Args:
        transactions (Union[List[Dict], Iterator[Dict]]): Список или итератор операций.

    Yields:
        Iterator[str]: Итератор по описаниям операций.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int):
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX, где X — цифра.

    Args:
        start (int): Начальный номер карты.
        end (int): Конечный номер карты.

    Yields:
        str: Сгенерированный номер карты.
    """
    for number in range(start, end + 1):
        # Форматирование номера карты
        card_number = f"{number:016d}"  # Форматирование с ведущими нулями
        formatted_card_number = " ".join([card_number[i:i + 4] for i in range(0, len(card_number), 4)])
        yield formatted_card_number

if __name__ == '__main__':
    transactions = [...]  # ваш список транзакций
    usd_transactions = filter_by_currency(transactions, "USD")
    descriptions = transaction_descriptions(transactions)
    card_numbers = card_number_generator(1, 5)
