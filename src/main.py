from src.masks import get_mask_account_card, get_mask_card_number

card_num = input("Введите номер карты: ")
print(get_mask_card_number(card_num))

account_num = input("Введите номер счета: ")
print(get_mask_account_card(account_num))

