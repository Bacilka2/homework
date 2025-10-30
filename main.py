from src.csv_reader import read_transactions_csv, read_transactions_excel
from src.masks import get_mask_account, get_mask_card_number
from src.utils import path_json
from config import ROOT_DIR

import os
from dotenv import load_dotenv

load_dotenv()


card_num = input("Введите номер карты: ")
print(get_mask_card_number(card_num))

account_num = input("Введите номер счета: ")
print(get_mask_account(account_num))

data = path_json(f"{ROOT_DIR}\\data\\operations.json")


def main():
    """Основная точка входа программы.
    Приветствует пользователя, выводит меню и вызывает обработчики
    в зависимости от выбора."""

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
                path_json()
            except TypeError:
                # Если функция ожидает параметры или отличается сигнатура
                path_json()
        else:
            print("Функция обработки JSON-файла не реализована в этом проекте.")
    elif user_input == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        if 'read_transactoins_csv' in globals():
            try:
                read_transactions_csv()
            except TypeError:
                read_transactions_csv()
        else:
            print("Функция обработки CSV-файла не реализована в этом проекте.")
    elif user_input == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        if 'read_transactions_excel' in globals():
            try:
                read_transactions_excel()
            except TypeError:
                read_transactions_excel()
        else:
            print("Функция обработки XLSX-файла не реализована в этом проекте.")
    else:
        print("Пользователь: Неправильный ввод. Пожалуйста, запустите программу снова и выберите 1, 2 или 3.")


if __name__ == "__main__":
    main()
