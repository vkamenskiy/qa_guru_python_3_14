import logging

import requests
from pytest_voluptuous import S

from schemas.user import users_list_schema


def test_get_users_list_schema():
    response = requests.get('https://reqres.in/api/users?', params={'page': 2})
    logging.info(response.json())
    assert S(users_list_schema) == response.json()


def test_users_default_count_on_page():
    response = requests.get('https://reqres.in/api/users?', params={'page': 1})
    per_page = response.json()['per_page']
    data = response.json()['data']

    assert per_page == 6
    assert len(data) == 6
    assert S(users_list_schema) == response.json()


