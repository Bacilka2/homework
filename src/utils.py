import json


def path_json(path):
    """функция апринимает на вход путь до
    JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding= "utf-8") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        return []

