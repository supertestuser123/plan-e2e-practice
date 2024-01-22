import requests
from src.config import base_url, cookie, token


REDISTRIBUTION_ALGORITHM = 'redistribution'
PLANNING_ALGORITHM = 'planning'


def test_get_list_all_file_config():
    url = f"{base_url}api/calculation-production-plan/file-configs/?algorithm_type={REDISTRIBUTION_ALGORITHM}&page=1"
    headers = {"Cookie": cookie,
               "accept": 'application/json',
               'X-CSRFToken': token
               }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Response is not in JSON format"
    json_data = response.json()

    assert 'results' in json_data, "Missing 'results' field in response"
    assert 'count' in json_data, "Missing 'count' field in response"
    assert 'per_page' in json_data, "Missing 'per_page' field in response"
    assert isinstance(json_data['results'], list), "'Results' is not a list in response"  # проверка что это список

    # Если резалтс не пустой, то идет проверка на наличие обязательных полей в первом элементе списка
    if json_data['results']:
        first_project = json_data['results'][0]
        assert 'id' in first_project, "Missing 'id' field in the first project"
        assert 'file_kind' in first_project, "Missing 'file_kind' field in the first project"
        assert 'name' in first_project, "Missing 'name' field in the first project"
        assert first_project['algorithm_type'] == REDISTRIBUTION_ALGORITHM
