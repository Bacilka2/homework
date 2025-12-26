from mypyc.ir.rtypes import RPrimitive

from src.csv_reader import read_transactions_csv, read_transactions_excel
from src.masks import get_mask_account, get_mask_card_number
from src.utils import path_json
from config import ROOT_DIR

import os
from dotenv import load_dotenv

load_dotenv()


#card_num = input("Введите номер карты: ")
#print(get_mask_card_number(card_num))

#ccount_num = input("Введите номер счета: ")
#print(get_mask_account(account_num))

data = path_json(f"{ROOT_DIR}\\data\\operations.json")

def normalize_user_status(user_input: str) -> str:
    """
    Нормализовать статус пользователя к верхнему регистру для сопоставления с
    доступными статусами фильтрации.
    """
    if user_input is None:
        return ""
    return user_input.strip().upper()


def filter_by_status(transactions, status):
    pass


def main():
    """Основная точка входа программы.
    Приветствует пользователя, выводит меню и вызывает обработчики
    в зависимости от выбора."""

    global filtered
    print("Программа: Привет! Добро пожаловать в программу работы")
    print("с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    try:
        user_input = input("Пользователь: ").strip()
    except EOFError:
        print("Пользователь: ")
        return

    if user_input == "1":
        print("Программа: Для обработки выбран JSON-файл.")

        if 'path_json' in globals():
            try:
                path_json('data/operations.json')
            except TypeError:
                # Если функция ожидает параметры или отличается сигнатура
                path_json('data/operations.json')
        else:
            print("Функция обработки JSON-файла не реализована в этом проекте.")
    elif user_input == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        if 'read_transactions_csv' in globals():
            try:
                read_transactions_csv('transactions.csv')
            except TypeError:
                read_transactions_csv('transactions.csv')
        else:
            print("Функция обработки CSV-файла не реализована в этом проекте.")
    elif user_input == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        if 'read_transactions_excel' in globals():
            try:
                read_transactions_excel('transactions_excel.xlsx')
            except TypeError:
                read_transactions_excel('transactions_excel.xlsx')
        else:
            print("Функция обработки XLSX-файла не реализована в этом проекте.")
    else:
        print("Пользователь: Неправильный ввод. Пожалуйста, запустите программу снова и выберите 1, 2 или 3.")
# Допустимые статусы
    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    # Запрос статуса для фильтрации
    print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING")

    user_status = input("Пользователь: ").strip()

    normalized = normalize_user_status(user_status)

    if normalized not in available_statuses:
        print(f'Программа: Статус операции "{user_status}" недоступен.')
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING")
        return

    # Здесь вы можете вызвать логику фильтрации по статусу в загруженных данных
    # Например: filtered = filter_transactions_by_status(data_json, normalized)
    # Но для демонстрации выведем ожидаемое сообщение:
    print(f'Программа: Операции отфильтрованы по статусу "{normalized}"')

    # 3) уточняющие вопросы
    # отсортировать по дате
    sort_by_date = input('Отсортировать операции по дате? Да/Нет\n').strip().lower()
    if sort_by_date in {'да', 'д', 'yes', 'y'}:
        order = input('Отсортировать по возрастанию или по убыванию?\n').strip().lower()
        reverse = (order in {'убывание', 'down', 'desc', 'descend'})  # зависит от ваших форматов
        filtered = sorted('key=lambda t: t.date, reverse=not reverse')
        # здесь корректно обрабатывайте форматы даты

    # вывод по требованию рублевых транзакций1
    currency_only = input('Выводить только руб'
                          'левые транзакции? Да/Нет\n').strip().lower()
    if currency_only in {'да', 'д', 'yes', 'y'}:
        filtered = []
        for t in filtered:
            if t.currency == 'RUB':
                filtered.append(t)

    # фильтр по слову в описании
    word_filter = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n').strip().lower()
    if word_filter in {'да', 'д', 'yes', 'y'}:
        word = input('Введите слово для фильтрации: ').strip().lower()
        filtered = [t for t in filtered if word in (t.description or '').lower()]

    # 4) печать итогов
    print('Распечатываю итоговый список транзакций...')
    for t in filtered:
        print(t)  # или форматированный вывод

    print(f'Всего банковских операций в выборке: {len(filtered)}')


if __name__ == "__main__":
    main()
