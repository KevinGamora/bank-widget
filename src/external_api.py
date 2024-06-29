"""
Модуль для работы с внешним API для получения курсов обмена валют.
"""

import os
from typing import Dict
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_exchange_rate(currency: str) -> float:
    """
    Получает текущий курс обмена заданной валюты к российскому рублю.

    Args:
        currency (str): Код валюты для конвертации.

    Returns:
        float: Курс обмена к российскому рублю.
    """
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # raises an exception for 4xx/5xx responses
    data: Dict[str, Dict[str, float]] = response.json()
    return data["rates"]["RUB"]

def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму из заданной валюты в российские рубли.

    Args:
        amount (float): Сумма денег в исходной валюте.
        currency (str): Код исходной валюты.

    Returns:
        float: Сумма денег в российских рублях.
    """
    if currency == "RUB":
        return amount
    rate = get_exchange_rate(currency)
    return amount * rate
