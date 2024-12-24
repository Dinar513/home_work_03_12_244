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
