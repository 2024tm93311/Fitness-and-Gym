import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Welcome to ACEest Fitness and Gym!" in rv.data

def test_get_members(client):
    rv = client.get('/members')
    assert rv.status_code == 200
    members = rv.get_json()
    assert isinstance(members, list)
    assert len(members) >= 1

def test_get_member_success(client):
    rv = client.get('/members/1')
    assert rv.status_code == 200
    member = rv.get_json()
    assert member["name"] == "Alice"

def test_get_member_not_found(client):
    rv = client.get('/members/999')
    assert rv.status_code == 404
    assert rv.get_json()["error"] == "Member not found"

def test_add_member_success(client):
    rv = client.post('/members', json={"name": "David", "membership": "Premium"})
    assert rv.status_code == 201
    member = rv.get_json()
    assert member["name"] == "David"
    assert member["membership"] == "Premium"

def test_add_member_invalid(client):
    rv = client.post('/members', json={})
    assert rv.status_code == 400
    assert rv.get_json()["error"] == "Invalid data"
