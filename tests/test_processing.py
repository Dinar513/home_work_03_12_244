from src.processing import filter_by_state, sort_by_date, transactions


def test_filter_by_state() -> None:
    # Тест на фильтрацию по статусу 'EXECUTED'
    executed_transactions = filter_by_state(transactions)
    assert executed_transactions == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ], "Ошибка: фильтрация по статусу 'EXECUTED'"

    # Тест на фильтрацию по статусу 'CANCELED'
    canceled_transactions = filter_by_state(transactions, "CANCELED")
    assert canceled_transactions == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ], "Ошибка: фильтрация по статусу 'CANCELED'"

    # Тест на отсутствие транзакций с указанным статусом
    no_transactions = filter_by_state(transactions, "PENDING")
    assert no_transactions == [], "Ошибка: ожидались пустые результаты для статуса 'PENDING'"

    # Тест на фильтрацию по статусу, который не существует
    empty_transactions = filter_by_state(transactions, "UNKNOWN")
    assert empty_transactions == [], "Ошибка: ожидались пустые результаты для статуса 'UNKNOWN'"


def test_sort_by_date() -> None:
    # Тест на сортировку по убыванию
    sorted_transactions_desc = sort_by_date(transactions)
    assert sorted_transactions_desc == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ], "Ошибка: сортировка по убыванию не сработала"

    # Тест на сортировку по возрастанию
    sorted_transactions_asc = sort_by_date(transactions, descending=False)
    assert sorted_transactions_asc == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ], "Ошибка: сортировка по возрастанию не сработала"

    # Тест на одинаковые даты
    same_date_transactions = [
        {"id": 1, "state": "EXECUTED", "date": "2022-01-01T12:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2022-01-01T12:00:00"},
    ]
    sorted_same_date = sort_by_date(same_date_transactions)
    assert sorted_same_date == same_date_transactions, "Ошибка: сортировка при одинаковых датах не сработала"

    # Тест на некорректный формат даты
    invalid_date_transactions = [
        {"id": 3, "state": "EXECUTED", "date": "invalid-date"},
    ]
    try:
        sort_by_date(invalid_date_transactions)
        assert False, "Ошибка: функция должна была выдать исключение при некорректной дате"
    except ValueError:
        pass  # Ожидаем, что будет выброшено исключение
