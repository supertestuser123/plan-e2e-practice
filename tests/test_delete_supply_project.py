import pytest
import requests
import src.config
from src.config import base_url, cookie, token, project_pk


# SPROCUR-2947
@pytest.mark.parametrize("project_pk", [project_pk])
def test_delete_supply_project(project_pk):
    url = base_url + "/api/supply-projects/" + str(src.config.project_pk) + "/"
    headers = {"accept": "application/json",
               "Cookie": cookie,
               "Content-Type": "application/json",
               'X-CSRFToken': token,
               "Referer": "https://splan-stage.samoletgroup.ru/admin/supplies/supplyproject/add/"}

    response = requests.delete(url, headers=headers)
    assert response.status_code == 204, f"Unexpected status code: {response.status_code}"
