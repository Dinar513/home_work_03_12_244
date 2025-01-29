import json
from pathlib import Path
from typing import Union
from json import JSONDecodeError
import logging

current_dir = Path(__file__).parent.parent.resolve()
operations_file_json = current_dir/'data'/'operations.json'
log_utils_file = current_dir/'logs'/'utils.log'


logger = logging.getLogger("list_dict_transactions")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_utils_file, mode='w', encoding="utf-8")
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.filemode = 'w'

def list_dict_transactions(operations_file_json: list) -> Union[list, dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """

    with open(operations_file_json, encoding="utf-8") as f:
        try:
            logger.info('Входные данные получены из JSON строки')
            operations_file = json.load(f)
        except json.JSONDecodeError as ex:
            logger.error(f'Произошла ошибка: {ex}')
            print('Ошибка декодирования файла')
            return []
        return operations_file


print(list_dict_transactions(operations_file_json))