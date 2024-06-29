from typing import List

from src.masks import mask_account_number, mask_card_number


def mask_info(info: str) -> str:
    """
    Маскирует номер карты или счета в предоставленной строке.

    Args:
        info (str): Строка, содержащая тип и номер карты или счета.

    Returns:
        str: Строка с замаскированным номером.

    Raises:
        ValueError: Если входная строка имеет неверный формат.
    """
    parts = info.split()
    if len(parts) < 2:
        raise ValueError("Неверный формат ввода")

    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower().startswith("счет"):
        masked_number = mask_account_number(number)
    else:
        masked_number = mask_card_number(number)

    return f"{name} {masked_number}"


class Widget:
    """
    Класс для представления виджета с транзакциями.

    Attributes:
        name (str): Имя виджета.
        value (float): Текущая сумма значений виджета.
        transactions (List[float]): Список транзакций, связанных с виджетом.
    """
    def __init__(self, name: str, value: float):
        """
        Инициализирует объект Widget.

        Args:
            name (str): Имя виджета.
            value (float): Начальное значение виджета.
        """
        self.name = name
        self.value = value
        self.transactions: List[float] = []

    def add_transaction(self, amount: float) -> None:
        """
        Добавляет транзакцию к виджету.

        Args:
            amount (float): Сумма транзакции.
        """
        self.transactions.append(amount)
        self.value += amount

    def display(self) -> str:
        """
        Возвращает строковое представление виджета.

        Returns:
            str: Строковое представление виджета.
        """
        return f"Widget {self.name}: {self.value}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Widget для разработчиков.

        Returns:
            str: Строковое представление объекта Widget.
        """
        return f"Widget(name={self.name}, value={self.value}, transactions={self.transactions})"
