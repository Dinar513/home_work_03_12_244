import pytest
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected_result",
    [
        ("Maestro 7000792289606361", "Maestro 7000 79  6361"),
        ("Счет 73654108430135874305", "Счет 7365 41  4305"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30  6758"),
        ("Visa Classic 73654108430135874305", "Visa Classic 7365 41  4305"),
        ("Visa Gold 7000792289606361", "Visa Gold 7000 79  6361"),
    ],
)
def test_mask_account_card(input_data: str, expected_result: str) -> None:
    assert mask_account_card(input_data) == expected_result


@pytest.mark.parametrize(
    "input_data, expected_result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-01-01T00:00:00", "01.01.2023"),
        ("2024-12-31T23:59:59", "31.12.2024"),
        ("2024-02-29T12:00:00", "29.02.2024"),
        ("", "отсутствует дата"),
        ("неверный формат", "неверный формат даты"),
    ],
)
def test_get_date(input_data: str, expected_result: str) -> None:
    assert get_date(input_data) == expected_result


@pytest.fixture
def all_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]