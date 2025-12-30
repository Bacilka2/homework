import re
from typing import List, Dict


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """ Функция возвращает список словарей из data, у которых в поле
    'description' содержится совпадение с регулярным выражением, сформированным
    из search. Поиск выполняется без учета регистра"""
    if not isinstance(data, list):
        raise TypeError("data must be a list of dicts")
    if search is None:
        return []

    try:
        pattern = re.compile(search, re.IGNORECASE)
    except re.error as e:

        raise ValueError(f"Invalid regular expression: {search}") from e

    result = []
    for item in data:
        if not isinstance(item, dict):
            continue
        description = item.get("description", "")
        if not isinstance(description, str):
            continue
        if pattern.search(description):
            result.append(item)

    return result
