import pytest


from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("arg, expected", [('Visa Platinum 7000792289606361', "Visa Platinum  7000 79** **** 6361"),
                                           ('Cчет  35383033474447895560', "Cчет  3538 3033 47** **** 5560"),])
def test_mask_account_card(arg, expected):
    assert mask_account_card(arg) == expected


@pytest.mark.parametrize("arg, expected", [("1981-11-17T00:00:01.136347", "17.11.1981"),
                                           ("1964-12-17T00:00:01.136347", "17.12.1964"), ])
def test_get_date(arg, expected):
    assert get_date(arg) == expected
