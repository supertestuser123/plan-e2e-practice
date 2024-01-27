import requests
from src.config import base_url, cookie, token, REDISTRIBUTION_ALGORITHM


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

    # Проверки на наличие ключей в ответе
    try:
        required_fields = ['results', 'count', 'per_page']
        for field in required_fields:
            assert field in json_data, f"Missing '{field}' field in response"
        assert isinstance(json_data.get('results'), list), "'Results' is not a list in response"
    except (AssertionError, TypeError):
        raise

    # Проверки на наличие ключей в первом объекте ответа
    try:
        if json_data['results']:
            first_project = json_data['results'][0]
            required_fields = ['id', 'name', 'title', 'file_kind', 'algorithm_type', 'is_file_reload']
            for field in required_fields:
                assert field in first_project, f"Missing '{field}' field in the first project"
    except (AssertionError, TypeError):
        raise

    # Проверки на то что переданный алгоритм соответствует алгоритму в запросе
    try:
        assert first_project['algorithm_type'] == REDISTRIBUTION_ALGORITHM
    except (AssertionError, TypeError):
        raise

    # Проверки на типы ключей
    try:
        type_checks = {
            'id': int,
            'name': str,
            'title': str,
            'file_kind': str,
            'algorithm_type': str,
            'is_file_reload': bool
        }
        for field, expected_type in type_checks.items():
            assert isinstance(first_project.get(field),
                              expected_type), f"'{field}' should be {expected_type} type"
    except (AssertionError, TypeError):
        raise

    # Проверка на количество ключей в ответе
    try:
        EXPECTED_KEYS_COUNT = 6
        assert len(first_project) == EXPECTED_KEYS_COUNT, "Изменение в количестве ключей в ответе"
    except (AssertionError, TypeError):
        raise
