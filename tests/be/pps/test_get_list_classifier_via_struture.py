import pytest
import requests
import src.config
from src.config import base_url, cookie, project_id, structure_id


# SPROCUR-14009
@pytest.mark.parametrize("structure_id, project_id", [(structure_id, project_id)])
def test_get_list_classifier_via_structure(project_id, structure_id):
    url = base_url + "/api/classifiers/" + str(src.config.project_id) + "/?structure_id=" + str(src.config.structure_id)
    headers = {"Cookie": cookie}
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
        assert 'name' in first_project, "Missing 'id' field in the first project"
        assert 'one_c_materials' in first_project, "Missing 'id' field in the first project"
        assert 'structure_guid' in first_project, "Missing 'structure_guid' field in the first project"
