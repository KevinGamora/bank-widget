# src/utils.py

from datetime import datetime


def format_date(date_str: str) -> str:
    """
    Преобразует строку даты и времени в форматированную строку даты.

    Args:
        date_str (str): Строка в формате 'YYYY-MM-DDTHH:MM:SS.ssssss'

    Returns:
        str: Строка в формате 'DD.MM.YYYY'
    """
    date = datetime.fromisoformat(date_str)
    return date.strftime('%d.%m.%Y')

def format_currency(value: float) -> str:
    """
    Форматирует число как денежную сумму.

    Args:
        value (float): Число для форматирования.

    Returns:
        str: Отформатированная денежная сумма.
    """
    return f"${value:,.2f}"
