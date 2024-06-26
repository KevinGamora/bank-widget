# main.py
import logging
from transactions import read_transactions_from_json, read_transactions_from_csv, read_transactions_from_xlsx, search_transactions, count_transactions_by_category


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    logger.info("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input("Пользователь: ").strip()
        if choice == '1':
            filepath = input("Введите путь к JSON-файлу: ").strip()
            transactions = read_transactions_from_json(filepath)
            print("Для обработки выбран JSON-файл.")
            break
        elif choice == '2':
            filepath = input("Введите путь к CSV-файлу: ").strip()
            transactions = read_transactions_from_csv(filepath)
            print("Для обработки выбран CSV-файл.")
            break
        elif choice == '3':
            filepath = input("Введите путь к XLSX-файлу: ").strip()
            transactions = read_transactions_from_xlsx(filepath)
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

    if not transactions:
        print("Не удалось загрузить транзакции из файла.")
        return

    statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: ").strip().upper()
        if status in statuses:
            transactions = [tx for tx in transactions if tx.get('status', '').upper() == status]
            print(f"Операции отфильтрованы по статусу \"{status}\".")
            break
        else:
            print(f"Статус операции \"{status}\" недоступен.")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    sort_by_date = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_by_date == 'да':
        order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        reverse = True if order == 'по убыванию' else False
        transactions.sort(key=lambda x: x.get('date', ''), reverse=reverse)

    only_rub = input("Выводить только рублевые тразакции? Да/Нет\nПользователь: ").strip().lower()
    if only_rub == 'да':
        transactions = [tx for tx in transactions if tx.get('currency', '').lower() == 'руб.']

    search_desc = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").strip().lower()
    if search_desc == 'да':
        search_string = input("Введите строку для поиска в описании транзакции: ").strip()
        transactions = search_transactions(transactions, search_string)

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for tx in transactions:
            print(f"{tx.get('date')} {tx.get('description')}\nСчет {tx.get('account')}\nСумма: {tx.get('amount')} {tx.get('currency')}")


if __name__ == "__main__":
    main()
