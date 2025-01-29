from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей по значению ключа `state`"""
    return [transaction for transaction in transactions if transaction.get("state") == state]


# Пример использования:
transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Выход функции со статусом по умолчанию 'EXECUTED':
executed_transactions = filter_by_state(transactions)
print(executed_transactions)

# Выход функции, если вторым аргументом передано 'CANCELED':
canceled_transactions = filter_by_state(transactions, "CANCELED")
print(canceled_transactions)


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по дате (по ключу 'date')"""
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=descending)


# Пример входных данных
transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Проверка работы функции
sorted_transactions = sort_by_date(transactions)
print(sorted_transactions)
