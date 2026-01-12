from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User
from app.schemas.user_schema import UserRegister, UserLogin, UserMe
from app.services.auth_service import AuthService
from app.auth.auth_dependencies import require_role
from app.auth.auth_dependencies import get_current_user_from_refresh, get_current_user
from app.auth.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(data: UserRegister, db: Session = Depends(get_db)):
    try:
        return AuthService.register(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/register-admin")
def register_admin(
    data: UserRegister,
    db: Session = Depends(get_db),
    _=Depends(require_role("ADMIN"))
):
    try:
        return AuthService.register_admin(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    try:
        return AuthService.login(db, data)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/refresh")
def refresh_token(
    payload=Depends(get_current_user_from_refresh),
    db: Session = Depends(get_db)
):
    user_id = payload["sub"]

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "access_token": create_access_token(user)
    }

@router.get("/me", response_model=UserMe)
def me(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = int(payload["sub"])
    return AuthService.me(db, user_id)