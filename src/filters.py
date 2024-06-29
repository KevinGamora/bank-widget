# src/filters.py

def filter_transactions_by_status(transactions, status):
    return [t for t in transactions if t.get('status') == status]


def sort_transactions_by_date(transactions, reverse=False):
    return sorted(transactions, key=lambda t: t.get('date'), reverse=reverse)


def filter_transactions_by_currency(transactions, currency):
    return [t for t in transactions if t.get('currency') == currency]


def search_transactions(transactions, query):
    return [t for t in transactions if query.lower() in t.get('description', '').lower()]
