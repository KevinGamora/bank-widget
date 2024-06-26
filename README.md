## Новый функционал

### Логирование

Добавлено логирование для следующих модулей:
- `masks`
- `utils`

Логи записываются в папку `logs` в корне проекта. Каждый модуль имеет свой отдельный лог-файл с расширением `.log`.

Формат записи лога включает метку времени, название модуля, уровень серьезности и сообщение, описывающее событие или ошибку, которые произошли.

### Примеры использования

Пример использования функций маскировки с логированием:

```python
from src.masks import mask_account_number, mask_card_number

masked_account = mask_account_number("1234567890123456")
masked_card = mask_card_number("1234567812345678")
