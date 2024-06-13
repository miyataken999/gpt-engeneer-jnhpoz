import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_user(client):
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json['id'] == 1
    assert response.json['name'] == 'John Doe'
    assert response.json['email'] == 'john@example.com'