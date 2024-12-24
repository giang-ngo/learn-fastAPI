from .utils import *
from ..routers.users import get_current_user, get_db
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'giangngo'
    assert response.json()['email'] == 'giangngo@gmail.com'
    assert response.json()['first_name'] == 'Giang'
    assert response.json()['last_name'] == 'Ngo'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '0123456789'


def test_change_password_success(test_user):
    response = client.put('/user/password', json={
        'password': 'testpassword',
        'new_password': 'newpassword'
    })
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put('/user/password', json={
        'password': 'wrong_password',
        'new_password': 'newpassword'
    })

    assert response.status_code == 401
    assert response.json() == {'detail': 'Error on change password'}


def test_change_phone_number_success(test_user):
    response = client.put('/user/phonenumber/9999')
    assert response.status_code == status.HTTP_204_NO_CONTENT
