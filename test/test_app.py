import json
import pytest
from app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    data = res.get_json()
    assert data["service"].startswith("ACEest")
    assert data["status"] == "ok"

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.data.decode().upper() == "OK"

def test_bmi_normal_category(client):
    payload = {"weight_kg": 70, "height_cm": 175}
    res = client.post("/bmi", data=json.dumps(payload), content_type="application/json")
    assert res.status_code == 200
    data = res.get_json()
    assert pytest.approx(data["bmi"], rel=1e-3) == 22.86
    assert data["category"] == "Normal"

def test_add_and_list_members(client):
    res = client.get("/members")
    assert res.status_code == 200
    assert res.get_json() == []

    res = client.post("/members", json={"name": "Riya", "age": 28})
    assert res.status_code == 201
    created = res.get_json()
    assert created["id"] == 1
    assert created["name"] == "Riya"

    res = client.get("/members")
    assert res.status_code == 200
    members = res.get_json()
    assert len(members) == 1
    assert members[0]["name"] == "Riya"
