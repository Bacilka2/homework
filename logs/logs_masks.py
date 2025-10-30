import logging


def get_mask_card_number(card_num: str, name=None) -> str:
    """Маска номера карты"""
    logger = logging.getLogger(name)
    logger.info("Запуск маскирования номера карты: %s", card_num)
    mask = "******"
    card_num_str = card_num[:6] + mask + card_num[12:]
    result = ""
    count = 0
    """Разделение номера карты для вывода по 4 символа через пробел"""
    for i in card_num_str:
        result += i
        count += 1
    if count % 4 == 0:
        result += " "
        logger.debug("Сформированная маска: %s", result.strip())
    return result.strip()


def get_mask_account(account_num: str, name=None) -> str:
    """Маска номера счета"""
    logger = logging.getLogger(name)
    logger.info("Запуск маскирования номера счета: %s", account_num)
    mask = "**"
    result: str | Any = mask + account_num[-4:]
    logger.debug("Сформированная маска счета: %s", result)
    return result
