import pytest
import requests


@pytest.fixture(scope='session')
def api_url():
    return 'https://jsonplaceholder.typicode.com'


@pytest.fixture(scope='session')
def session():
    return requests.Session()


def test_get_posts(api_url, session):
    response = session.get(f'{api_url}/posts')
    assert response.status_code == 200
    assert len(response.json()) == 100


def test_post_post(api_url, session):
    data = {'title': 'test post', 'body': 'test body', 'userId': 1}
    response = session.post(f'{api_url}/posts', data=data)
    assert response.status_code == 201
    assert response.json()['title'] == data['title']


def test_delete_post(api_url, session):
    response = session.delete(f'{api_url}/posts/1')
    assert response.status_code == 200
    assert response.json() == {}


def test_get_nonexistent_post(api_url, session):
    response = session.get(f'{api_url}/posts/999')
    assert response.status_code == 404


def test_post_invalid_data(api_url, session):
    invalid_data = {'invalid': 'data'}
    response = session.post(f'{api_url}/posts', json=invalid_data)
    assert response.status_code == 201


def test_delete_nonexistent_post(api_url, session):
    response = session.delete(f'{api_url}/posts/999')
    assert response.status_code == 200
