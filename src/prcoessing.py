from datetime import datetime
from typing import List, Dict

list_of_dict=[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
              {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
              {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
              {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(list_of_dict: list, state='EXECUTED') -> list:

    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению."""

    filtered_list = []
    for dict in list_of_dict:
        if dict.get('state') == state:
          filtered_list.append(dict)
        else:
         continue
    return filtered_list

print(filter_by_state(list_of_dict))




operations_sort_by_date: List[Dict[str, str]] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

def sort_by_date(operations: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """Функция возвращает новый список, отсортированный по дате """

    sorted_operations = operations.copy()
    sorted_operations.sort(key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)

    return sorted_operations
print(sort_by_date(operations_sort_by_date))