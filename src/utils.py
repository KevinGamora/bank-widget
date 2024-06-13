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
