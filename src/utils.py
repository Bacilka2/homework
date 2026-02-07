import json


def path_json(path):
    """функция апринимает на вход путь до
    JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
            empty_list = []
            for row in data:
                transaction = {
                    "id": row.get("id"),
                    "state": row.get("state"),
                    "date": row.get("date"),
                    "amount": row.get("operationAmount",{}).get("amount",0),
                    "currency_name": row.get("operationAmount",{}).get("currency",{}).get("name"),
                    "currency_code": row.get("operationAmount",{}).get("currency",{}).get("code"),
                    "from": row.get("from"),
                    "to": row.get("to"),
                    "description": row.get("description")}
                empty_list.append(transaction)
            return empty_list
    except json.JSONDecodeError:
        return []
