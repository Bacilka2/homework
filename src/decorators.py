import logging
import time
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


def log(filename=None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                time_1 = time.time()
                result = func(*args, **kwargs)
                time_2 = time.time()
                name_func = func.__name__
                if filename:
                    with open(filename, 'a', encoding="utf-8") as file:
                        file.write(f"Начало: {time_1} \nФункция{name_func}ок. Результат:{result}\nКонец: {time_2}\n\n")
                        file.close()
                    return f"Начало: {time_1} \nФункция {name_func} ок. Результат: {result}\nКонец: {time_2}\n\n"
                else:
                    print(f"Начало: {time_1} \nФункция {name_func} ок. Результат: {result}\nКонец: {time_2}")
            except Exception as e:
                name_func = func.__name__
                if filename:
                    file = open(filename, 'a', encoding='utf-8')
                    file.write(f"{name_func} error: {e}. Inputs: {args}, {kwargs}")
                    file.close()
                    return f"{name_func} error: {e}. Inputs: {args}, {kwargs}"
                else:
                    print(f"{name_func} error: {e}. Inputs: {args}, {kwargs}")
        return wrapper
    return my_decorator


# @log(filename="mylog.txt")
@log()
def my_function(x, y):
    return x + y


@log()
def second_fun(x, y):
    print(x / y)


second_fun(5, 1)
