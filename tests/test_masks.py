import unittest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    # Тест 1: стандартный случай
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361", "Ошибка в стандартном случае"

    # Тест 2: минимальная длина номера карты
    assert get_mask_card_number("123456") == "1234 56** **** 3456", "Ошибка для минимальной длины"

    # Тест 3: слишком короткий номер карты
    assert get_mask_card_number("123") == "Некорректный номер карты", "Ошибка для короткого номера карты"

    # Тест 4: пустая строка
    assert get_mask_card_number("") == "Некорректный номер карты", "Ошибка для пустой строки"


class test_get_mask_account(unittest.TestCase):
    def test_normal_account(self):
        """Тест нормального номера счета"""
        account_num = "73654108430135874305"
        expected = "**4305"
        self.assertEqual(get_mask_account(account_num), expected)

    def test_short_account(self):
        """Тест короткого номера счета"""
        account_num = "123"  # Меньше 20 символов
        with self.assertRaises(ValueError):
            get_mask_account(account_num)

    def test_empty_account(self):
        """Тест пустой строки"""
        account_num = ""
        with self.assertRaises(ValueError):
            get_mask_account(account_num)

    def test_non_numeric_account(self):
        """Тест строки с нечисловыми символами"""
        account_num = "abcd1234123412341234"
        with self.assertRaises(ValueError):
            get_mask_account(account_num)
