import pandas as pd

def read_transactions_csv(filepath: str) -> pd.DataFrame:
    """
    Считывает финансовые операции из CSV-файла.
    """
    return pd.read_csv(filepath)

def read_transactions_excel(filepath: str, sheet_name: str = 0) -> pd.DataFrame:
    """
    Считывает финансовые операции из Excel
    """
    x = pd.read_excel(filepath, sheet_name=sheet_name)
    return x
