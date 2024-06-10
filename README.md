# Проект: Bank Widget

## Описание

Этот проект представляет собой виджет для управления банковскими операциями.

## Новые функции

### Модуль generators

Модуль `generators` содержит следующие функции:

- **filter_by_currency(transactions, currency_code)**: Возвращает итератор по операциям с указанной валютой.
- **transaction_descriptions(transactions)**: Возвращает итератор по описаниям операций.
- **card_number_generator(start, end)**: Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.

#### Примеры использования

**filter_by_currency**

```python
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions)["id"])
