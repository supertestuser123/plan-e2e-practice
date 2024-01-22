import requests
from src.config import base_url, cookie, token

expected_keys_count = 9


def test_get_list_all_file_config():
    url = f"{base_url}api/calculation-production-plan/last-successful-event-calc-production-plan/"
    headers = {"Cookie": cookie,
               "accept": 'application/json',
               'X-CSRFToken': token
               }
    response = requests.get(url, headers=headers)
    # Проверки на код ответа
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Response is not in JSON format"
    json_data = response.json()

    if json_data:
        # Проверки на поля в ответе
        assert 'id' in json_data, "Missing 'id' field in the first project"
        assert 'guid' in json_data, "Missing 'guid' field in the first project"
        assert 'status' in json_data, "Missing 'status' field in the first project"
        assert 'user_id' in json_data, "Missing 'user_id' field in the first project"
        assert 'calculation_type' in json_data, "Missing 'calculation_type' field in the first project"
        assert 'error_description' in json_data, "Missing 'error_description' field in the first project"
        assert 'results' in json_data, "Missing 'results' field in the first project"
        assert 'updated' in json_data, "Missing 'updated' field in the first project"
        assert 'created' in json_data, "Missing 'created' field in the first project"

        # Проверки на типы полей
        assert isinstance(json_data["id"], int)
        assert isinstance(json_data["guid"], str)
        assert isinstance(json_data["status"], str)
        assert isinstance(json_data["user_id"], int)
        assert isinstance(json_data["calculation_type"], str)
        assert isinstance(json_data["results"], list)
        assert isinstance(json_data["updated"], str)
        assert isinstance(json_data["created"], str)

        # Проверка, что количество ключей в ответе соответствует ожидаемому
        assert len(json_data) == expected_keys_count, "Изменение в количестве ключей в ответе"
