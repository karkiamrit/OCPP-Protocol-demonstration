from fastapi import Depends, HTTPException, status
from app.auth.security import verify_token, oauth2_scheme
from app.auth.models import TokenData

def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenData:
    return verify_token(token)

def get_current_active_user(current_user: TokenData = Depends(get_current_user)) -> TokenData:
    if current_user.role not in ["admin", "user"]:  # Adjust roles as needed
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    return current_user

def role_required(required_role: str):
    def role_checker(current_user: TokenData = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions",
            )
        return current_user
    return role_checker
