import requests

from helper.data_type_checker import check_data_type
from src.config import base_url, cookie, token


REDISTRIBUTION_ALGORITHM = 'redistribution'
PLANNING_ALGORITHM = 'planning'
SUB_MODE = 'mixed'
expected_keys_count = 12


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
        if json_data:
            assert 'id' in json_data, "Missing 'id' field"
            assert 'guid' in json_data, "Missing 'guid' field"
            assert 'status' in json_data, "Missing 'status' field"
            assert 'user_id' in json_data, "Missing 'user_id' field"
            assert 'calculation_type' in json_data, "Missing 'calculation_type' field"
            assert 'sub_mode' in json_data, "Missing 'sub_mode' field"
            assert 'file_configs' in json_data, "Missing 'file_configs' field"
            assert 'files' in json_data, "Missing 'files' field"
            assert 'error_description' in json_data, "Missing 'error_description' field"
            assert 'results' in json_data, "Missing 'results' field"
            assert 'updated' in json_data, "Missing 'updated' field"
            assert 'created' in json_data, "Missing 'created' field"
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
        assert isinstance(json_data["id"], int), "'id' should be int type"
        assert isinstance(json_data["guid"], str), "'guid' should be str type"
        assert isinstance(json_data["status"], str), "'status' should be str type"
        assert isinstance(json_data["user_id"], int), "'user_id' should be int type"
        assert isinstance(json_data["calculation_type"], str), "'calculation_type' should be int type"
        assert isinstance(json_data["sub_mode"], str), "'sub_mode' should be int type"
        assert isinstance(json_data["file_configs"], list), "'file_configs' should be list type"
        try:
            check_data_type(json_data, "files", list)
            check_data_type(json_data, "error_description", dict)
            check_data_type(json_data, "results", list)
        except AssertionError as e:
            print(e)
            raise
        assert isinstance(json_data["updated"], str), "'updated' should be int type"
        assert isinstance(json_data["created"], str), "'created' should be int type"
    except (AssertionError, TypeError):
        raise
    #
    # # Проверка на количество ключей в ответе
    # try:
    #     assert len(first_project) == expected_keys_count, "Изменение в количестве ключей в ответе"
    # except (AssertionError, TypeError):
    #     raise
