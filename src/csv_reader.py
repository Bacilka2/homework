import pandas as pd
from typing import List, Dict


def read_transactions_csv(filepath: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла и возвращает список словарей.
    """
    df = pd.read_csv(filepath)
    return df.to_dict(orient='records')


def read_transactions_excel(filepath: str, sheet_name: str = 0) -> List[Dict]:
    """
    Считывает финансовые операции из Excel и возвращает список словарей.
    """

    df = pd.read_excel(filepath, sheet_name=sheet_name)
    return df.to_dict(orient='records')
