from src.masks import get_mask_account, get_mask_card_number

card_num = input("Введите номер карты: ")
print(get_mask_card_number(card_num))

account_num = input("Введите номер счета: ")
print(get_mask_account(account_num))


