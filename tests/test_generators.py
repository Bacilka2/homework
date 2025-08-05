#import pytest
#from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


#def test_filter_by_currency(generators_transactions, generators_transactions_usd):
 #   assert filter_by_currency(generators_transactions, "USD") == iter( generators_transactions_usd)


import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency(generators_transactions, generators_transactions_usd):
    assert list(filter_by_currency(generators_transactions, "USD")) == list(generators_transactions_usd)


def test_transaction_description():
    transactions = [{ "description": "Перевод со счета на счет"}, {"description": "Перевод организации"}, ]
    expected_descriptions = [  "Перевод со счета на счет",  "Перевод организации"]

    # Преобразовать итератор в список для сравнения
    assert list(transaction_descriptions(transactions)) == expected_descriptions


def test_transaction_descriptions_empty():
    transactions = []
    expected_descriptions = []

    # Проверка с пустым списком
    assert list(transaction_descriptions(transactions)) == expected_descriptions



def test_card_number_generator():
    expected = [(f'{str(number).zfill(16)[:4]} '
                  f'{str(number).zfill(16)[4:8]} '
                  f'{str(number).zfill(16)[8:12]}'
                f' {str(number).zfill(16)[12:]}') for number in range(3, 41)]

    generated = list(card_number_generator(3, 40))
    assert generated == expected
