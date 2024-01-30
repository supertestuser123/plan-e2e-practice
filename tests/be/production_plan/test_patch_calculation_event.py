import json

import requests

from helper.data_type_checker import check_data_type
from src.config import base_url, cookie, token, TEST_EVENT_GUID


def test_patch_calculate_event():
    url = f"{base_url}api/calculation-production-plan/event-calc-production-plan/{TEST_EVENT_GUID}/"

    headers = {"Cookie": cookie,
               "accept": 'application/json',
               'X-CSRFToken': token,
               "Referer": "https://splan-stage.samoletgroup.ru"
               }

    data = '{"results": ["test"], "status": "CANCELED"}'
    response = requests.patch(url, headers=headers, data=data)

    try:
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Response is not in JSON format"
    except (AssertionError, TypeError):
        raise

    json_data = response.json()

    # Проверки на наличие ключей в ответе
    try:
        required_fields = ['id', 'guid', 'status', 'files', 'calculation_type', 'error_description', 'results',
                           'updated', 'results', 'created', 'user_id']
        if json_data:
            for field in required_fields:
                assert field in json_data, f"Missing '{field}' field"
    except (AssertionError, TypeError):
        raise

    # Проверки на то что переданная дата записалась в ивенте
    try:
        data = json.loads(data)
        assert json_data['status'] == data["status"]
        assert json_data['results'] == data["results"]
    except (AssertionError, TypeError):
        raise

    # Проверки на типы ключей
    try:
        type_checks = {
            'id': int,
            'guid': str,
            'status': str,
            'calculation_type': str,
            'updated': str,
            'created': str,
            'user_id': int,
        }
        for field, expected_type in type_checks.items():
            assert isinstance(json_data.get(field),
                              expected_type), f"'{field}' should be {expected_type} type"
            try:
                check_data_type(json_data, "files", list)
                check_data_type(json_data, "error_description", dict)
                check_data_type(json_data, "results", list)
            except AssertionError as e:
                print(e)
                raise
    except (AssertionError, TypeError):
        raise

    # Проверка на количество ключей в ответе
    try:
        EXPECTED_KEYS_COUNT = 10
        assert len(json_data) == EXPECTED_KEYS_COUNT, "Изменение в количестве ключей в ответе"
    except (AssertionError, TypeError):
        raise
