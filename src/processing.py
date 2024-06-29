from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Args:
        data (List[Dict]): Список словарей с данными.
        state (str): Значение для фильтрации по ключу 'state'. По умолчанию 'EXECUTED'.

    Returns:
        List[Dict]: Новый список, содержащий только те словари, у которых ключ 'state' содержит переданное значение.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по значению ключа 'date'.

    Args:
        data (List[Dict]): Список словарей с данными.
        reverse (bool): Порядок сортировки, по умолчанию по убыванию (True).

    Returns:
        List[Dict]: Новый список, отсортированный по значению ключа 'date'.
    """
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
