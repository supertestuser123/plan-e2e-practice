import requests
from src.config import base_url, cookie, token


REDISTRIBUTION_ALGORITHM = 'redistribution'
PLANNING_ALGORITHM = 'planning'
expected_keys_count = 6


def test_get_list_all_file_config():
    url = f"{base_url}api/calculation-production-plan/file-configs/?algorithm_type={REDISTRIBUTION_ALGORITHM}&page=1"
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

    # Проверки на наличие полей в ответе
    try:
        assert 'results' in json_data, "Missing 'results' field in response"
        assert 'count' in json_data, "Missing 'count' field in response"
        assert 'per_page' in json_data, "Missing 'per_page' field in response"
        assert isinstance(json_data['results'], list), "'Results' is not a list in response"
    except (AssertionError, TypeError):
        raise

    try:
        if json_data['results']:
            first_project = json_data['results'][0]
            assert 'id' in first_project, "Missing 'id' field in the first project"
            assert 'name' in first_project, "Missing 'name' field in the first project"
            assert 'title' in first_project, "Missing 'title' field in the first project"
            assert 'file_kind' in first_project, "Missing 'file_kind' field in the first project"
            assert 'algorithm_type' in first_project, "Missing 'algorithm_type' field in the first project"
            assert 'is_file_reload' in first_project, "Missing 'is_file_reload' field in the first project"
    except (AssertionError, TypeError):
        raise

    # Проверки на то что переданный алгоритм соответствует алгоритму в ответе
    try:
        assert first_project['algorithm_type'] == REDISTRIBUTION_ALGORITHM
    except (AssertionError, TypeError):
        raise

    # Проверки на типы ответов
    try:
        assert isinstance(first_project['id'], int)
        assert isinstance(first_project['name'], str)
        assert isinstance(first_project["title"], str)
        assert isinstance(first_project["file_kind"], str)
        assert isinstance(first_project["algorithm_type"], str)
        assert isinstance(first_project["is_file_reload"], bool)
    except (AssertionError, TypeError):
        raise

    # Проверка на количество элементов
    try:
        assert len(first_project) == expected_keys_count, "Изменение в количестве ключей в ответе"
    except (AssertionError, TypeError):
        raise
