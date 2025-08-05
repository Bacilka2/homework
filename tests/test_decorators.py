from src.decorators import log


@log()
def test_func(x):
    return 10 / x

@log('logfile.txt')
def test_error():
    raise ValueError("Что-то пошло не так")