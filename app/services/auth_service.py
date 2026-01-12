from fastapi import HTTPException
from app.repositories.user_repository import UserRepository
from app.auth.password_handler import hash_password, verify_password
from app.auth.jwt_handler import create_access_token, create_refresh_token
from app.models.user_model import User

class AuthService:

    @staticmethod
    def register(db, data):
        if UserRepository.get_by_email(db, data.email):
            raise ValueError("Email already registered")

        user = User(
            name=data.name,
            email=data.email,
            password=hash_password(data.password)
        )

        return UserRepository.create(db, user)
    
    @staticmethod
    def register_admin(db, data):
        if UserRepository.get_by_email(db, data.email):
            raise ValueError("Email already registered")

        user = User(
            name=data.name,
            email=data.email,
            role="ADMIN",
            password=hash_password(data.password)
        )

        return UserRepository.create(db, user)

    @staticmethod
    def login(db, data):
        user = UserRepository.get_by_email(db, data.email)
        if not user or not verify_password(data.password, user.password):
            raise ValueError("Invalid credentials")

        return {
            "access_token": create_access_token(user),
            "refresh_token": create_refresh_token(user)
        }
    
    
    @staticmethod
    def me(db, user_id: int):
        user = UserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        return user
