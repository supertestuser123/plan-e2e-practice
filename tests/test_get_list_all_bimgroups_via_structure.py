import pytest
import requests

import src.config
from src.config import base_url, cookie, structure_id, group_id

# SPROCUR-14008


@pytest.mark.parametrize("structure_id, group_id", [(structure_id, group_id)])
def test_get_list_all_bimgroups_via_structure(structure_id, group_id):
    url = base_url + "/api/bim-groups/for-structure/" + str(src.config.structure_id) + "/" + str(src.config.group_id) + "/"
    headers = {"Cookie": cookie}
    response = requests.get(url, headers=headers)
    json_data = response.json()

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Response is not in JSON format"

    # Если ответ не пустой, то идет проверка на наличие обязательных полей в ответе
    if json_data:
        assert 'name' in json_data, "Missing 'id' field in the project"
        assert 'bim_group_ids' in json_data, "Missing 'name' field in the project"
        assert 'group_guid' in json_data, "Missing 'guid' field in the project"
        assert json_data['group_id'] == group_id
