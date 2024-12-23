from typing import Union


def get_mask_account(account_num: Union[str]) -> str:
    """Функция для получения маски номера счета"""
    return f"**{account_num[-4:]}"


print(get_mask_account("73654108430135874305"))



def get_mask_card_number(card_num: Union[str]) -> str:
    """Функция для получения маски номера карты"""
    if not isinstance(card_num, str) or len(card_num) < 6:
        return "Некорректный номер карты"
    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"

print(get_mask_card_number("7000792289606361"))