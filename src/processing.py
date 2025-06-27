
from typing import List, Dict

def filter_by_state(
    transactions: List[Dict],
    state: str = 'EXECUTED'
) -> List[Dict]:
    return [tx for tx in transactions if tx.get('state') == state]

def sort_by_date(
    transactions: List[Dict],
    reverse: bool = True
) -> List[Dict]:
    return sorted(transactions, key=lambda x: x.get('date', ''), reverse=reverse)