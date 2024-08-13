from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.ocpp_service import MyOCPPProtocol
import json

router = APIRouter()

@router.websocket("/ws/ocpp")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    ocpp_protocol = MyOCPPProtocol(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            await ocpp_protocol.handle_message(message)
    except WebSocketDisconnect:
        print("Client disconnected")
