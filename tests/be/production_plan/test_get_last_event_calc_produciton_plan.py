import requests
from src.config import base_url, cookie, token

expected_keys_count = 9


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
        if json_data:
            assert 'id' in json_data, "Missing 'id' field"
            assert 'guid' in json_data, "Missing 'guid' field"
            assert 'status' in json_data, "Missing 'status' field"
            assert 'user_id' in json_data, "Missing 'user_id' field"
            assert 'calculation_type' in json_data, "Missing 'calculation_type' field"
            assert 'error_description' in json_data, "Missing 'error_description' field"
            assert 'results' in json_data, "Missing 'results' field"
            assert 'updated' in json_data, "Missing 'updated' field"
            assert 'created' in json_data, "Missing 'created' field"
    except (AssertionError, TypeError):
        raise
    # Проверки на типы ключей
    try:
        assert isinstance(json_data["id"], int), "'id' should be int type"
        assert isinstance(json_data["guid"], str), "'guid' should be string type"
        assert isinstance(json_data["status"], str), "'status' should be string type"
        assert isinstance(json_data["user_id"], int), "'user_id' should be int type"
        assert isinstance(json_data["calculation_type"], str), "'calculation_type' should be str type"
        try:
            if json_data["error_description"] is None:
                assert True
            else:
                assert isinstance(json_data["error_description"], dict), "'error_description' should be dict type"
        except (AssertionError, TypeError):
            raise
        try:
            if json_data["results"] is None:
                assert True
            else:
                assert isinstance(json_data["results"], list), "'results' should be list type"
        except (AssertionError, TypeError):
            raise
        assert isinstance(json_data["updated"], str), "'updated' should be string type"
        assert isinstance(json_data["created"], str), "'created' should be string type"
    except (AssertionError, TypeError):
        raise

    # Проверка, что количество ключей в ответе соответствует ожидаемому
    try:
        assert len(json_data) == expected_keys_count, "Extra or missing key"
    except (AssertionError, TypeError):
        raise
