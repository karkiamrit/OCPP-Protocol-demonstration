import json
from fastapi.testclient import TestClient
from nea_backend.nea_backend.main import app

client = TestClient(app)

def test_websocket():
    with client.websocket_connect("/ws/ocpp") as websocket:
        websocket.send_text('{"action": "BootNotification", "chargePointModel": "ModelX", "chargePointVendor": "VendorY"}')
        response = websocket.receive_text()
        assert json.loads(response) == {"status": "Accepted", "currentTime": "2024-08-13T12:00:00Z"}
