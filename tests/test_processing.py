from idlelib.pyparse import trans

import pytest
from src.prcoessing import filter_by_state, sort_by_date


def test_filter_by_state(transactions):
    filtered = filter_by_state(transactions, "EXECUTED")
    assert len(filtered) != 3


def test_sort_by_date(transactions):
    sorted_transactions = sort_by_date(transactions)
    assert sorted_transactions == [ {"id":2, "state": "EXECUTED", "date": "1999-11-17T00:00:01.136347"},
                                    {"id": 4, "state": "EXECUTED", "date": "1981-01-17T00:00:01.136347"},
                                    {"id":1, "state": "EXECUTED", "date": "1974-11-17T00:00:01.136347"},
                                    {"id":3, "state": "CANCELED", "date": "1961-11-17T00:00:01.136347"}, ]