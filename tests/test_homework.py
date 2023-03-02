import requests
from pytest_voluptuous import S

from schemas.user import created_user, updated_user, registered_user


def test_single_user_not_found():
    response = requests.get('https://reqres.in/api/users/23')

    assert response.status_code == 404


def test_create_new_user():
    response = requests.post(
        'https://reqres.in/api/users',
        {
            "name": "vladislav",
            "job": "mcdonalds"
        }
    )
    name = response.json()['name']
    job = response.json()['job']

    assert name == 'vladislav'
    assert job == 'mcdonalds'
    assert response.status_code == 201
    assert S(created_user) == response.json()


def test_update_user_job():
    response = requests.put(
        'https://reqres.in/api/users/9',
        {
            "name": "morpheus",
            "job": "zion resident"
        }
    )
    name = response.json()['name']
    job = response.json()['job']

    assert name == 'morpheus'
    assert job == 'zion resident'
    assert response.status_code == 200
    assert S(updated_user) == response.json()


def test_delete_user():
    response = requests.delete('https://reqres.in/api/users/2')

    assert response.status_code == 204
    assert len(response.content) == 0


def test_register_new_user_successful():
    response = requests.post(
        'https://reqres.in/api/register',
        {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
    )
    user_id = response.json()['id']
    result = requests.get(f'https://reqres.in/api/users/{user_id}')
    email = result.json()['data']['email']

    assert response.status_code == 200
    assert result.status_code == 200
    assert S(registered_user) == response.json()
    assert email == 'eve.holt@reqres.in'
