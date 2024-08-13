from pydantic import BaseModel
from typing import Optional

# Example models for OCPP messages

class BootNotificationRequest(BaseModel):
    chargePointModel: str
    chargePointVendor: str

class BootNotificationResponse(BaseModel):
    status: str
    currentTime: str

class AuthorizeRequest(BaseModel):
    idTag: str

class AuthorizeResponse(BaseModel):
    idTagInfo: dict  # You may define a more detailed structure based on OCPP specs

# Add other OCPP message models as needed
