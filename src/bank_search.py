import re
from collections import Counter
from typing import List, Dict

def search_operations(data: List[Dict], query: str, key: str = "description", exact: bool = False) -> List[Dict]:

    if not data:
        return []

    if exact:
        pattern = re.compile(rf"^{re.escape(query)}$", re.IGNORECASE)
    else:
        pattern = re.compile(rf"{re.escape(query)}", re.IGNORECASE)

    found = []
    for item in data:
        value = item.get(key, "")
        if value is None:
            continue
        if pattern.search(str(value)):
            found.append(item)
    return found


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:

    # Приведение категорий к уникальному набору для скорости и предсказуемости
    category_set = set(categories)

    # Счетчик по всем операциям, где ключ — значение из поля description
    counts = Counter()

    for op in data:
        desc = op.get("description")
        if desc is None:
            continue
        # если описание совпадает с одной из категорий, учитываем
        if desc in category_set:
            counts[desc] += 1

    # Приведем результат к виду: {категория: количество}

    result = {cat: counts.get(cat, 0) for cat in categories}
    return result