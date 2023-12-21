import requests
import src.config
from src.config import base_url, cookie, token


# SPROCUR-2944
def test_get_post_supply_project():
    url = base_url + "/api/supply-projects/"
    headers = {"accept": "application/json",
               "Cookie": cookie,
               "Content-Type": "application/json",
               'X-CSRFToken': token,
               "Referer": "https://splan-stage.samoletgroup.ru/admin/supplies/supplyproject/add/"}

    response = requests.post(url, headers=headers, json=src.config.payload)
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Response is not in JSON format"
    json_data = response.json()

    if json_data:
        assert 'id' in json_data, "Missing 'id' field in the first project"
        assert 'otif' in json_data, "Missing 'project' field in the first project"
        assert json_data['project']['id'] == src.config.payload['project_id']
        assert json_data['executor'] == src.config.payload['executor']
        assert json_data['address'] == src.config.payload['address']
        assert json_data['comment'] == src.config.payload['comment']
