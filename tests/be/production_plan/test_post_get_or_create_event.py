import requests
from helper.data_type_checker import check_data_type
from src.config import base_url, cookie, token, NUMBER_OF_FILES_IN_CONFIG, REDISTRIBUTION_ALGORITHM, SUB_MODE


def test_post_get_or_create():
    url = f"{base_url}api/calculation-production-plan/get-or-create-event-calc-production-plan/?calculation_type={REDISTRIBUTION_ALGORITHM}&sub_mode={SUB_MODE}"
    headers = {"Cookie": cookie,
               "accept": 'application/json',
               'X-CSRFToken': token,
               "Referer": "https://splan-stage.samoletgroup.ru"
               }
    response = requests.post(url, headers=headers)

    # Проверки на код ответа
    try:
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Response is not in JSON format"
    except (AssertionError, TypeError):
        raise

    json_data = response.json()

    # Проверки на наличие ключей в ответе
    try:
        required_fields = ['id', 'guid', 'status', 'user_id', 'calculation_type', 'sub_mode', 'file_configs', 'files',
                           'error_description', 'results', 'updated', 'created']
        if json_data:
            for field in required_fields:
                assert field in json_data, f"Missing '{field}' field"
    except (AssertionError, TypeError):
        raise

    # Проверки на то что переданный алгоритм и подтип соответствует алгоритму в запросе
    try:
        assert json_data['calculation_type'] == REDISTRIBUTION_ALGORITHM
        assert json_data['sub_mode'] == SUB_MODE
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
            'sub_mode': str,
            'file_configs': list,
            'updated': str,
            'created': str
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
        EXPECTED_KEYS_COUNT = 12
        assert len(json_data) == EXPECTED_KEYS_COUNT, "Изменение в количестве ключей в ответе"
    except (AssertionError, TypeError):
        raise

    # Проверка на количество конфигов в file_configs
    try:
        assert len(json_data["file_configs"]) == NUMBER_OF_FILES_IN_CONFIG, "Изменение в количестве ключей в ответе"
    except (AssertionError, TypeError):
        raise
