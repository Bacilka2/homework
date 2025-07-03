from src.masks import get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """  Обрабатывает информацию о картах и счетах, и выводит маскировку. """
    if "счет" in account_card.lower():
        number_card = account_card[-10:]
        masked_card = mask_account_card(number_card)
        return f"Счет {masked_card}"
    else:
        name_card = account_card[-16:]
        masked = get_mask_card_number(name_card)
        bank_name = account_card[:-16]
    return f"{bank_name} {masked}"


def get_date(data_number: str) -> str:
    """   Вывести дату в формате "ДД.ММ.ГГГГ"  """
    correct = data_number[8:10] + "." + data_number[5:7] + "." + data_number[:4]
    return correct


if __name__ == '__main__':
    print(mask_account_card('Visa Platinum 7000792289606361'))

    print(mask_account_card('"Cчет"  35383033474447895560'))

    print(get_date("1981-11-17T00:00:01.136347"))