# tests/test_endpoints.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_configuration():
    response = client.post("/create_configuration", json={"country_code": "IN", "business_name": "Test Business", "registration_number": "12345"})
    assert response.status_code == 200
    assert response.json()["country_code"] == "IN"

def test_get_configuration():
    response = client.get("/get_configuration/IN")
    assert response.status_code == 200
    assert response.json()["country_code"] == "IN"

def test_update_configuration():
    response = client.post("/update_configuration", json={"country_code": "IN", "business_name": "Updated Business Name"})
    assert response.status_code == 200
    assert response.json()["business_name"] == "Updated Business Name"

def test_delete_configuration():
    response = client.delete("/delete_configuration/IN")
    assert response.status_code == 200
    assert response.json()["message"] == "Configuration deleted successfully"
