from src.masks import get_mask_card_number
from typing import Union


def test_get_mask_card_number():
    # Тест 1: стандартный случай
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361", "Ошибка в стандартном случае"

    # Тест 2: минимальная длина номера карты
    assert get_mask_card_number("123456") == "1234 56** **** 3456", "Ошибка для минимальной длины"

    # Тест 3: слишком короткий номер карты
    assert get_mask_card_number("123") == "Некорректный номер карты", "Ошибка для короткого номера карты"

    # Тест 4: пустая строка
    assert get_mask_card_number("") == "Некорректный номер карты", "Ошибка для пустой строки"



