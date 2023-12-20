import pytest
import requests

import src.config
from src.config import base_url, cookie, structure_id


# SPROCUR-14010
@pytest.mark.parametrize("structure_id", [structure_id])
def test_get_project_queue_structure(structure_id):
    url = base_url + "/api/dashboard/breadcrumbs/" + str(src.config.structure_id) + "/"
    headers = {"Cookie": cookie}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Response is not in JSON format"
    json_data = response.json()

    # Если резалтс не пустой, то идет проверка на наличие обязательных полей в первом элементе списка
    if json_data:
        assert 'project_id' in json_data, "Missing 'id' field in the first project"
        assert 'queue_id' in json_data, "Missing 'project' field in the first project"
        assert 'structure_id' in json_data, "Missing 'otif' field in the first project"
        assert json_data['structure_id'] == structure_id
