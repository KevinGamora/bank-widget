from src.masks import mask_card_number, mask_account_number

def mask_info(info: str) -> str:
    """
    Маскирует номер карты или счета в предоставленной строке.

    Аргументы:
        info (str): Строка, содержащая тип и номер карты или счета.

    Возвращает:
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
