import logging
import os
from src.utils import read_transactions_from_json, read_transactions_from_csv, read_transactions_from_xlsx
from src.filters import filter_transactions_by_status, sort_transactions_by_date, filter_transactions_by_currency, search_transactions
from collections import Counter


# Настройка логирования
if not os.path.exists('logs'):
    os.makedirs('logs')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join('logs', 'main.log'), mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта: ")
    if choice == '1':
        filepath = input("Введите путь к JSON-файлу: ")
        transactions = read_transactions_from_json(filepath)
        logger.info(f"Загружены транзакции из JSON-файла: {filepath}")
    elif choice == '2':
        filepath = input("Введите путь к CSV-файлу: ")
        transactions = read_transactions_from_csv(filepath)
        logger.info(f"Загружены транзакции из CSV-файла: {filepath}")
    elif choice == '3':
        filepath = input("Введите путь к XLSX-файлу: ")
        transactions = read_transactions_from_xlsx(filepath)
        logger.info(f"Загружены транзакции из XLSX-файла: {filepath}")
    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")
        logger.error("Неверный выбор формата файла")
        return

    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ").upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_transactions_by_status(transactions, status)
            logger.info(f"Отфильтрованы транзакции по статусу: {status}")
            break
        else:
            print(f"Статус операции '{status}' недоступен.")
            logger.warning(f"Статус операции '{status}' недоступен")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice == 'да':
        order = input("Отсортировать по возрастанию или по убыванию? ").lower()
        reverse = (order == "по убыванию")
        transactions = sort_transactions_by_date(transactions, reverse)
        logger.info(f"Транзакции отсортированы по дате в порядке: {'убывания' if reverse else 'возрастания'}")

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if currency_choice == 'да':
        transactions = filter_transactions_by_currency(transactions, 'RUB')
        logger.info("Отфильтрованы только рублевые транзакции")

    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if search_choice == 'да':
        search_term = input("Введите слово для поиска в описании: ")
        transactions = search_transactions(transactions, search_term)
        logger.info(f"Отфильтрованы транзакции по слову в описании: {search_term}")

    if transactions:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            print(f"{transaction['date']} {transaction['description']}")
            print(f"Сумма: {transaction['amount']} {transaction['currency']}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        logger.info("Не найдено ни одной транзакции, подходящей под условия фильтрации")

if __name__ == "__main__":
    main()
