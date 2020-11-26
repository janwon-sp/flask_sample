import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    test_client = app.test_client()
    yield test_client
    test_client.delete()

def test_index(client):
    result = client.get('/')
    assert b'Hello World' == result.data

def test_good(client):
    result = client.get('/good')
    assert b'Good' == result.data