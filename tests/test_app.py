import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"ACEest Fitness Manager" in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json["status"] == "UP"

def test_add_task(client):
    response = client.post('/add', data={"title": "Evening Yoga"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Evening Yoga" in response.data