import requests
from src.config import base_url, cookie, token, REDISTRIBUTION_ALGORITHM, FILE_KIND, TEST_EVENT_GUID


def test_post_get_or_create():
    url = f"{base_url}api/calculation-production-plan/files/{TEST_EVENT_GUID}/?file_kind={FILE_KIND}&algorithm_type={REDISTRIBUTION_ALGORITHM}"

    headers = {"Cookie": cookie,
               "accept": 'application/json',
               'X-CSRFToken': token,
               "Referer": "https://splan-stage.samoletgroup.ru"
               }

    files = {'upload_file': ('Стоп-лист.xlsx', open('../../../files/Стоп-лист.xlsx', 'rb'),
                             'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}

    response = requests.post(url, headers=headers, files=files)

    try:
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Response is not in JSON format"
    except (AssertionError, TypeError):
        raise

    json_data = response.json()

    # Проверки на наличие ключей в ответе
    try:
        required_fields = ['id', 'name', 'title', 'file_kind', 'event_id', 'event_guid', 'url', 'created',
                           'updated']
        if json_data:
            for field in required_fields:
                assert field in json_data, f"Missing '{field}' field"
    except (AssertionError, TypeError):
        raise

    # Проверки на то что переданный алгоритм и подтип соответствует алгоритму в запросе
    try:
        assert json_data['event_guid'] == TEST_EVENT_GUID
        assert json_data['file_kind'] == FILE_KIND
    except (AssertionError, TypeError):
        raise

    # Проверки на типы ключей
    try:
        type_checks = {
            'id': int,
            'name': str,
            'title': str,
            'event_id': int,
            'event_guid': str,
            'url': str,
            'created': str,
            'updated': str,
        }
        for field, expected_type in type_checks.items():
            assert isinstance(json_data.get(field),
                              expected_type), f"'{field}' should be {expected_type} type"
    except (AssertionError, TypeError):
        raise

    # Проверка на количество ключей в ответе
    try:
        EXPECTED_KEYS_COUNT = 9
        assert len(json_data) == EXPECTED_KEYS_COUNT, "Изменение в количестве ключей в ответе"
    except (AssertionError, TypeError):
        raise
