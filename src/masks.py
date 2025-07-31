def get_mask_card_number(card_num: str) -> str:
    """Маска номера карты"""
    mask = "******"
    card_num_str = card_num[:6] + mask + card_num[12:]
    result = ""
    count = 0
    """Разделение номера карты для выведения по 4 символа через пробел"""
    for i in card_num_str:
        result += i
        count += 1
        if count % 4 == 0:
            result += " "
    return result.strip()


def get_mask_account(account_num: str) -> str:
    """Маска номера счета"""
    mask = "**"
    result = mask + account_num[-4:]
    return result


print(get_mask_account('64686473678894779589'))
