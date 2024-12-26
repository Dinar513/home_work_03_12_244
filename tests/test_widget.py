import unittest
from src.widget import get_date, mask_account_card


class Test_Mask_Account_Card(unittest.TestCase):

    def test_mask_maestro(self) -> None:
        self.assertEqual(mask_account_card("Maestro 7000792289606361"), "Maestro 7000 79** ****  6361")

    def test_masks_chet(self) -> None:
        self.assertEqual(mask_account_card("Счет 73654108430135874305"), "Счет 7365 41** ****  4305")

    def test_mask_master_card(self) -> None:
        self.assertEqual(mask_account_card("MasterCard 7158300734726758"), "MasterCard 7158 30** ****  6758")

    def test_mask_visa_classic(self) -> None:
        self.assertEqual(mask_account_card("Visa Classic 73654108430135874305"), "Visa Classic 7365 41** ****  4305")

    def test_mask_visa_gold(self) -> None:
        self.assertEqual(mask_account_card("Visa Gold 7000792289606361"), "Visa Gold 7000 79** ****  6361")

    def test_unknown_type(self) -> None:
        with self.assertRaises(ValueError) as context:
            mask_account_card("UnknownType 1234567890123456")
        self.assertEqual(str(context.exception), "Неизвестный тип карты или счета")


def test_get_date() -> None:
    # Тесты на корректные входные данные
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024", "Ошибка при обработке корректной даты с временем"
    assert get_date("2024-03-11") == "11.03.2024", "Ошибка при обработке корректной даты без времени"

    # Тесты на некорректные форматы
    assert get_date("2024/03/11") == "неверный формат даты", "Ошибка при обработке некорректного формата даты"
    assert get_date("2024-03") == "неверный формат даты", "Ошибка при обработке неполной даты"
    assert get_date("March 11, 2024") == "неверный формат даты", "Ошибка при обработке некорректного формата даты"

    # Тесты на пустую или отсутствующую дату
    assert get_date("") == "отсутствует дата", "Ошибка при обработке пустой строки"
    assert get_date(None) == "отсутствует дата", "Ошибка при обработке значения None"

    # Тесты на граничные случаи
    assert get_date("0001-01-01") == "01.01.0001", "Ошибка при обработке минимальной даты"
    assert get_date("9999-12-31T23:59:59") == "31.12.9999", "Ошибка при обработке максимальной даты с временем"
