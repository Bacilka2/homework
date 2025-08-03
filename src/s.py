from src.generators import filter_by_currency

transactions = []
usd_transactions = filter_by_currency(transactions, "USD")

f