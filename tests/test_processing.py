import pytest
from processing import filter_by_state, sort_by_date

# Пример данных для тестирования
sample_transactions = [
    {"id": 1, "state": "EXECUTED", "date": "2023-10-01"},
    {"id": 2, "state": "PENDING", "date": "2023-09-30"},
    {"id": 3, "state": "EXECUTED", "date": "2023-09-29"},
    {"id": 4, "state": "FAILED", "date": "2023-10-02"},
]

def test_filter_by_state_default():
    # По умолчанию фильтр по 'EXECUTED'
    result = filter_by_state(sample_transactions)
    ids = [trans["id"] for trans in result]
    assert ids == [1, 3]

def test_filter_by_state_custom():
    # Фильтр по 'PENDING'
    result = filter_by_state(sample_transactions, 'PENDING')
    ids = [trans["id"] for trans in result]
    assert ids == [2]

def test_filter_by_state_no_match():
    # Нет транзакций с таким статусом
    result = filter_by_state(sample_transactions, 'CANCELLED')
    assert result == []

def test_sort_by_date_descending():
    # По умолчанию сортировка по убыванию (reverse=True)
    sorted_trans = sort_by_date(sample_transactions)
    dates = [trans["date"] for trans in sorted_trans]
    assert dates == sorted(dates, reverse=True)

def test_sort_by_date_ascending():
    # Сортировка по возрастанию
    sorted_trans = sort_by_date(sample_transactions, reverse=False)
    dates = [trans["date"] for trans in sorted_trans]
    assert dates == sorted(dates)

def test_sort_with_missing_date():
    # Проверка обработки транзакции без ключа 'date'
    transactions_with_missing_date = [
        {"id": 1, "date": "2023-10-01"},
        {"id": 2},
        {"id": 3, "date": "2023-09-29"}
    ]
    sorted_list = sort_by_date(transactions_with_missing_date)
    # Транзакции без 'date' получат пустую строку и будут в начале при сортировке по возрастанию
    assert sorted_list[0]["id"] == 2

# Можно добавить дополнительные тесты по необходимости