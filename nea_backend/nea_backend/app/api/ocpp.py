from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from app.auth.dependencies import get_current_user, role_required
from app.services.ocpp_service import MyOCPPProtocol
import json
from nea_backend.nea_backend.app.auth.models import TokenData

router = APIRouter()

@router.websocket("/ws/ocpp")
async def websocket_endpoint(websocket: WebSocket, current_user: TokenData = Depends(get_current_user)):
    await websocket.accept()
    ocpp_protocol = MyOCPPProtocol(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            await ocpp_protocol.handle_message(message)
    except WebSocketDisconnect:
        print("Client disconnected")
