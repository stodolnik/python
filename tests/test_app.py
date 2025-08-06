from http import HTTPStatus

from fast_zero.schemas import Userpublic, UserSchema


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = Userpublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


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
