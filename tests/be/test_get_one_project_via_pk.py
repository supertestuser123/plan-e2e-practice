import pytest
import requests
from src.config import base_url, cookie, pk


# SPROCUR-2946
@pytest.mark.parametrize("pk", [pk])
def test_get_one_project_via_pk(pk):
    url = base_url + "/api/supply-projects/" + str(pk) + "/"
    headers = {"Cookie": cookie}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Response is not in JSON format"
    json_data = response.json()

    assert json_data['id'] == pk
    # Если проект не пустой, то идет проверка
    # на наличие обязательных полей в ответе
    if json_data['project']:
        project = json_data['project']
        assert 'id' in project, "Missing 'id' field in the project"
        assert 'name' in project, "Missing 'name' field in the project"
        assert 'guid' in project, "Missing 'guid' field in the project"
        assert 'construction' in project, "Missing 'construction' field in the project"
        assert 'otif' in project, "Missing 'otif' field in the project"
