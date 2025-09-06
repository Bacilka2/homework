import json
import logging


def path_json(path):
    """функция принимает на вход путь до
JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    logger = logging.getLogger(name)
    logger.info("Попытка открыть JSON-файл: %s", path)
    try:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
            logger.info("Успешно считаны данные из файла: %s", path)
        return data
    except FileNotFoundError:
        logger.error("Файл не найден: %s", path)
        return []