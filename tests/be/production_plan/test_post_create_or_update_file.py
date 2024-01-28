import os

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
    print(response.status_code)
    print(response.text)
