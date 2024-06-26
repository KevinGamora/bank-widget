## Новый функционал

### Поддержка чтения данных из файлов JSON, CSV и XLSX

Проект теперь поддерживает чтение данных о финансовых транзакциях из файлов форматов JSON, CSV и XLSX.

#### Примеры использования

```python
from utils import read_transactions_from_json, read_transactions_from_csv, read_transactions_from_xlsx

# Чтение данных из JSON-файла
transactions_json = read_transactions_from_json('path/to/transactions.json')

# Чтение данных из CSV-файла
transactions_csv = read_transactions_from_csv('path/to/transactions.csv')

# Чтение данных из XLSX-файла
transactions_xlsx = read_transactions_from_xlsx('path/to/transactions.xlsx')
