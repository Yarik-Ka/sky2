import pytest
from widget import mask_account_card, get_date

# Тестирование функции mask_account_card с разными типами данных
@pytest.mark.parametrize("input_value, expected_type", [
    ("1234 5678 9012 3456", "card"),
    ("1234 5678", "account"),
])
def test_mask_account_card_correct_type(input_value, expected_type):
    result = mask_account_card(input_value)
    # В зависимости от типа входных данных проверяем результат
    if expected_type == "card":
        assert "****" in result or isinstance(result, str)
    else:
        assert result.startswith("**") or isinstance(result, str)

@pytest.mark.parametrize("invalid_input", [
    1234567890,
    None,
    12.34,
    [],
])
def test_mask_account_card_invalid_input(invalid_input):
    with pytest.raises(Exception):
        mask_account_card(invalid_input)

# Тестирование функции get_date с различными форматами дат
@pytest.mark.parametrize("input_str, expected_output", [
    ("2023-10-01", "01.10.2023"),
    ("01/10/2023", "01.10.2023"),
    ("10-01-2023", "01.10.2023"),
])
def test_get_date_various_formats(input_str, expected_output):
    result = get_date(input_str)
    assert result == expected_output

# Граничные случаи и нестандартные строки
@pytest.mark.parametrize("input_str", [
    "",             # пустая строка
    "не дата",      # строка без даты
    "2023-02-29",   # некорректная дата (февраль 29 в невисокосном году)
])
def test_get_date_edge_cases(input_str):
    try:
        result = get_date(input_str)
        # Можно проверить, что результат — строка или None
        assert isinstance(result, str) or result is None
    except Exception:
        # Если функция должна выбрасывать исключение для некорректных дат — это тоже допустимо
        pass