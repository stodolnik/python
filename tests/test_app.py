from http import HTTPStatus

from fast_zero.app import UserList, Userpublic, UserSchema


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_create_user(client):
    user_input = UserSchema(
        username='Lucas', email='lucas@example.com', password='teste'
    )
    user_output = Userpublic(id=1, username='Lucas', email='lucas@example.com')

    response = client.post('/users/', json=user_input.model_dump())

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == user_output.model_dump()


def test_read_users(client):
    response = client.get('/users/')
    user_output = UserList(
        users=[Userpublic(id=1, username='Lucas', email='lucas@example.com')]
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_output.model_dump()


def test_read_user(client):
    user_output = Userpublic(id=1, username='Lucas', email='lucas@example.com')

    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_output.model_dump()


def test_update_user(client):
    user_input = UserSchema(
        username='Lucas', email='lucas@example.com', password='teste'
    )
    user_output = Userpublic(id=1, username='Lucas', email='lucas@example.com')

    response = client.put('/users/1', json=user_input.model_dump())

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_output.model_dump()


def test_delete_user(client):
    response = client.delete('/users/1')
    user_output = {'message': 'User deleted'}

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_output
