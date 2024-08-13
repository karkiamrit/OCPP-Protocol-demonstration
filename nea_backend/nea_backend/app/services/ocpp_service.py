from ocpp.routing import on
from ocpp import OCPPProtocol
from app.schemas.ocpp_models import BootNotificationRequest, BootNotificationResponse
import json
from nea_backend.nea_backend.app.schemas.ocpp_models import AuthorizeRequest, AuthorizeResponse

class MyOCPPProtocol(OCPPProtocol):
    async def handle_message(self, message: dict):
        if 'action' in message:
            action = message['action']
            handler = getattr(self, f'handle_{action.lower()}', None)
            if handler:
                response = await handler(message)
                await self.websocket.send_text(json.dumps(response))
            else:
                await self.websocket.send_text(json.dumps({"status": "Unknown Action"}))
        else:
            await self.websocket.send_text(json.dumps({"status": "Invalid Message Format"}))

    async def handle_bootnotification(self, message: dict):
        request = BootNotificationRequest(**message)
        # Handle the request, process it, and create a response
        response = BootNotificationResponse(status="Accepted", currentTime="2024-08-13T12:00:00Z")
        return response.model_dump()

    async def handle_authorize(self, message: dict):
        request = AuthorizeRequest(**message)
        # Handle authorization, potentially validate idTag
        response = AuthorizeResponse(idTagInfo={"status": "Accepted"})
        return response.model_dump()
