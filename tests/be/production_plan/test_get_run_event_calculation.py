import requests

from src.config import base_url, cookie, token, TEST_RUN_EVENT_GUID


def test_get_run_event_calc_production_plan():
    url = f"{base_url}api/calculation-production-plan/run-event-calc-production-plan/{TEST_RUN_EVENT_GUID}/"
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
        required_fields = ['guid', 'detail', 'status']
        if json_data:
            for field in required_fields:
                assert field in json_data, f"Missing '{field}' field"
    except (AssertionError, TypeError):
        raise
    #
    # Проверки на типы ключей
    try:
        type_checks = {
            'guid': str,
            'detail': str,
            'status': str,
        }
        for field, expected_type in type_checks.items():
            assert isinstance(json_data.get(field), expected_type), f"'{field}' should be {expected_type} type"
    except (AssertionError, TypeError):
        raise

    # Проверка, что количество ключей в ответе соответствует ожидаемому
    try:
        EXPECTED_KEYS_COUNT = 3
        assert len(json_data) == EXPECTED_KEYS_COUNT, "Extra or missing key"
    except (AssertionError, TypeError):
        raise

    # Проверка, что переданные параметры ожидаются в ответе
    try:
        assert json_data['guid'] == TEST_RUN_EVENT_GUID
        assert json_data['status'] == 'PENDING'
    except (AssertionError, TypeError):
        raise
