def check_data_type(data, key, expected_type):
    """Функция проверки ключей, значение которых может иметь два поведения"""
    try:
        if data[key] is None:
            assert True
        else:
            assert isinstance(data[key], expected_type), f"'{key}' should be {expected_type} type"
    except (AssertionError, TypeError):
        raise
