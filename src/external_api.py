import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_exchange_rate(currency: str) -> float:
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # raises an exception for 4xx/5xx responses
    data = response.json()
    return data["rates"]["RUB"]


def convert_to_rub(amount: float, currency: str) -> float:
    if currency == "RUB":
        return amount
    rate = get_exchange_rate(currency)
    return amount * rate
