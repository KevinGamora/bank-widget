from src.masks import mask_account_number, mask_card_number

def mask_info(info: str) -> str:
    """
    Маскирует номер карты или счета в предоставленной строке.

    Args:
        info (str): Строка, содержащая тип и номер карты или счета.

    Returns:
        str: Строка с замаскированным номером.
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
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def display(self) -> str:
        return f"Widget {self.name}: {self.value}"

    def add_transaction(self, amount: int):
        self.value += amount
