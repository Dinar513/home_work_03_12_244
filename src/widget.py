from src.masks import get_mask_card_number, get_mask_account
from typing import Union

def mask_account_card(card_number:Union[str, int]) ->str:
    if 'Счет' in card_number:
        return 'Счет ' + get_mask_account(card_number)
    if 'Maestro' in card_number:
        return 'Maestro' + ' ' + get_mask_card_number(card_number.split()[-1])
    if 'MasterCard' in card_number:
        return 'MasterCard' + ' ' + get_mask_card_number(card_number.split()[-1])
    if 'Visa Classic' in card_number:
        return 'Visa Classic' + ' ' + get_mask_card_number(card_number.split()[-1])
    if 'Visa Platinum' in card_number:
        return 'Visa Platinum' + ' ' + get_mask_card_number(card_number.split()[-1])
    if 'Visa Gold' in card_number:
        return 'Visa Gold' + ' ' + get_mask_card_number(card_number.split()[-1])



print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Visa Classic 73654108430135874305"))
print(mask_account_card("Visa Gold 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_string):
    # Разбиваем строку по символу 'T'
    date_part = date_string.split('T')[0]

    # Разделяем дату на составляющие (год, месяц, день)
    year, month, day = date_part.split('-')

    # Форматируем дату в нужный формат "ДД.ММ.ГГГГ"
    date_string = f"{day}.{month}.{year}"

    return date_string
print(get_date("2024-03-11T02:26:18.671407"))#


