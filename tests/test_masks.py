import pytest
from masks import get_mask_card_number, get_mask_account

# Тесты для get_mask_card_number
@pytest.mark.parametrize("card_number, expected", [
    ("1234 5678 9012 3456", "1234 ** **** 3456"),
    ("1234567890123456", "1234 ** **** 3456"),
    ("1234 5678 9012 34", None),  # меньше 16 символов после очистки -> ошибка
    ("1234 5678 9012 34567890", "1234 ** **** 7890"), # длинный номер
])
def test_get_mask_card_number_valid_and_invalid(card_number, expected):
    if expected is None:
        with pytest.raises(ValueError):
            get_mask_card_number(card_number)
    else:
        result = get_mask_card_number(card_number)
        assert result == expected

# Тесты для get_mask_account
@pytest.mark.parametrize("account_number, expected", [
    ("1234 5678", "**5678"),
    ("12345678", "**5678"),
    ("1234 56", None),  # меньше 8 символов -> ошибка
    ("9876 5432 1098", "**1098"), # более длинный номер
])
def test_get_mask_account_valid_and_invalid(account_number, expected):
    if expected is None:
        with pytest.raises(ValueError):
            get_mask_account(account_number)
    else:
        result = get_mask_account(account_number)
        assert result == expected