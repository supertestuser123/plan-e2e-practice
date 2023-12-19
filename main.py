# import json
# import requests
#
#
#
#
# def test_get_list_all_supply_projects():
#     url = base_url + "/api/supply-projects/"
#     headers = {"Cookie": cookie}
#     response = requests.get(url, headers= headers)
#     json_data = response.json()
#     json_response = json.dumps(json_data, indent=4)
#
#     assert response.status_code == 200
#     assert 'results' in json_data
#     assert 'count' in json_data
#     assert 'per_page' in json_data
#     assert 'id' in json_response
#     assert 'project' in json_response
#
# test_get_list_all_supply_projects()
#
# #SPROCUR-2941
# def test_get_one_project_via_id(id):
#     url = base_url + "/api/supply-projects/?project_id=" + str(id)
#     headers = {"Cookie": cookie}
#     response = requests.get(url, headers= headers)
#     json_data = response.json()
#     json_response = json.dumps(json_data, indent=4)
#
#     #проверка что в ответе именно тот id который передаем в запросе
#     get_project_id = json.loads(json_response)
#     project_id = get_project_id['results'][0]['project']['id']
#
#     assert response.status_code == 200
#     assert project_id == id
#
# test_get_one_project_via_id(69)

# #SPROCUR-2946
# def test_get_one_project_via_pk(pk):
#     url = base_url + "/api/supply-projects/" + str(pk)+"/"
#
#     headers = {"Cookie": cookie}
#     response = requests.get(url, headers= headers)
#     json_data = response.json()
#     json_response = json.dumps(json_data, indent=4)
#
#     # проверка что в ответе именно тот id который передаем в запросе
#     get_project_pk = json.loads(json_response)
#     project_pk = get_project_pk['id']
#
#     assert response.status_code == 200
#     assert project_pk == pk

# test_get_one_project_via_pk(130)

#SPROCUR-14008
def test_get_list_all_bimgroups_via_structure(structure_id, group_id):
    url = base_url + "/api/bim-groups/for-structure/" + str(structure_id) +"/" + str(group_id) +"/"
    headers = {"Cookie": cookie}
    response = requests.get(url, headers= headers)
    json_data = response.json()
    json_response = json.dumps(json_data, indent=4)

    # проверка что в ответе именно тот group_id который передаем в запросе
    get_group_id = json.loads(json_response)
    group = get_group_id['group_id']

    assert response.status_code == 200
    assert 'name' in json_response
    assert 'group_guid' in json_response
    assert group == group_id

test_get_list_all_bimgroups_via_structure(21296, 52)