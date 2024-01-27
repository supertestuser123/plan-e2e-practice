import requests

from helper.data_type_checker import check_data_type
from src.config import base_url, cookie, token


def test_get_last_event_calc_production_plan():
    url = f"{base_url}api/calculation-production-plan/last-event-calc-production-plan/"
    headers = {"Cookie": cookie,
               "accept": 'application/json',
               'X-CSRFToken': token
               }
    response = requests.get(url, headers=headers)

    # Проверки на код ответа
    try:
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Response is not in JSON format"
    except (AssertionError, TypeError):
        raise

    json_data = response.json()

    # проверяем блок наличия ключей в ответе
    try:
        required_fields = ['id', 'guid', 'status', 'user_id', 'calculation_type', 'error_description', 'results',
                           'updated', 'created']
        if json_data:
            for field in required_fields:
                assert field in json_data, f"Missing '{field}' field"
    except (AssertionError, TypeError):
        raise

    # Проверки на типы ключей
    try:
        type_checks = {
            'id': int,
            'guid': str,
            'status': str,
            'user_id': int,
            'calculation_type': str,
            'updated': str,
            'created': str
        }
        for field, expected_type in type_checks.items():
            assert isinstance(json_data.get(field), expected_type), f"'{field}' should be {expected_type} type"
        try:
            check_data_type(json_data, "error_description", dict)
            check_data_type(json_data, "results", list)
        except AssertionError as e:
            print(e)
            raise
    except (AssertionError, TypeError):
        raise

    # Проверка, что количество ключей в ответе соответствует ожидаемому
    try:
        EXPECTED_KEYS_COUNT = 9
        assert len(json_data) == EXPECTED_KEYS_COUNT, "Extra or missing key"
    except (AssertionError, TypeError):
        raise
