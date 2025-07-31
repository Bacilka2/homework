import pytest


@pytest.fixture
def transactions():
    return [{"id":1, "state": "EXECUTED", "date": "1974-11-17T00:00:01.136347"},
            {"id":2, "state": "EXECUTED", "date": "1999-11-17T00:00:01.136347"},
            {"id":3, "state": "CANCELED", "date": "1961-11-17T00:00:01.136347"},
            {"id":4, "state": "EXECUTED", "date": "1981-01-17T00:00:01.136347"}]