from fastapi.testclient import TestClient
from nea_backend.nea_backend.main import app

client = TestClient(app)

def test_login():
    response = client.post(
        "/auth/token", data={"username": "testuser", "password": "password"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
