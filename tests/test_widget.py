import unittest
from src.widget import mask_account_card, get_date


class test_mask_account_card(unittest.TestCase):
    def test_mask_maestro(self):
        self.assertEqual(mask_account_card("Maestro 7000792289606361"), "Maestro 7000 79** **** 6361")

    def test_mask_schet(self):
        self.assertEqual(mask_account_card("Счет 73654108430135874305"), "Счет 7365 41** **** 4305")

    def test_mask_master_card(self):
        self.assertEqual(mask_account_card("MasterCard 7158300734726758"), "MasterCard 7158 30** **** 6758")

    def test_mask_visa_classic(self):
        self.assertEqual(mask_account_card("Visa Classic 73654108430135874305"), "Visa Classic 7365 41** **** 4305")

    def test_mask_visa_gold(self):
        self.assertEqual(mask_account_card("Visa Gold 7000792289606361"), "Visa Gold 7000 79** **** 6361")

    def test_unknown_type(self):
        with self.assertRaises(ValueError) as context:
            mask_account_card("UnknownType 1234567890123456")
        self.assertEqual(str(context.exception), "Неизвестный тип карты или счета")



