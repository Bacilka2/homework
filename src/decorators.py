import logging

from functools import wraps


def setup_logger(filename=None):
    """Настройка логгера."""
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Создание обработчика для записи в файл или вывода в консоль
    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def log(filename=None):
    """Декоратор для логирования выполнения функции."""

    logger = setup_logger(filename)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f'Starting execution of {func.__name__} with args: {args} and kwargs: {kwargs}')
            try:
                result = func(*args, **kwargs)
                logger.info(f'Finished execution of {func.__name__}. Result: {result}')
                return result
            except Exception as e:
                logger.error(f'Error in {func.__name__}: {type(e).__name__} - {e}. Args: {args}, Kwargs: {kwargs}')
                raise

        return wrapper

    return decorator