from typing import List, Dict
import re


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Подсчитать количество банковских операций по заданным категориям"""
    pattern_map = {}
    for c in categories:
        pattern_map[c] = re.compile(re.escape(str(c)), re.IGNORECASE)


    counts = {cat: 0 for cat in categories}


    for item in data:
        desc = str(item.get("description", ""))
        for cat, pat in pattern_map.items():
            if pat.search(desc):
                counts[cat] += 1

                break

    return counts