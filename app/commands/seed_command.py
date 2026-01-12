import json
from pathlib import Path

from app.database import SessionLocal
from app.models.user_model import User
from app.repositories.user_repository import UserRepository
from app.auth.password_handler import hash_password


SEED_FILE = Path(__file__).parent.parent / "seed" / "seed_data.json"


def run_seed():
    print("🌱 Ejecutando seed...")

    db = SessionLocal()

    try:
        with open(SEED_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        users = data.get("users", [])

        for user_data in users:
            existing_user = UserRepository.get_by_email(
                db, user_data["email"]
            )

            if existing_user:
                print(f"✔ Usuario ya existe: {user_data['email']}")
                continue

            user = User(
                name=user_data["name"],
                email=user_data["email"],
                role=user_data["role"],
                password=hash_password(user_data["password"]),
            )

            UserRepository.create(db, user)
            print(f"➕ Usuario creado: {user.email}")

        print("✅ Seed finalizado correctamente")

    finally:
        db.close()
