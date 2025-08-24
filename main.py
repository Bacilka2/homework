from src.masks import get_mask_account, get_mask_card_number
from src.utils import path_json
from config import ROOT_DIR

card_num = input("Введите номер карты: ")
print(get_mask_card_number(card_num))

account_num = input("Введите номер счета: ")
print(get_mask_account(account_num))

data = path_json(f"{ROOT_DIR}\\data\\operations.json")

