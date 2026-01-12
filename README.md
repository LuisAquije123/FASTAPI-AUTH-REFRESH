# 🚀 FastAPI Authentication API

API de autenticación y gestión de usuarios desarrollada con **FastAPI**, **SQLite** y **JWT**, con soporte para **roles (ADMIN / USER)**, **hashing seguro de contraseñas (Argon2)** y arquitectura limpia.

---

## 🧱 Tecnologías usadas

- **FastAPI**
- **SQLite**
- **SQLAlchemy**
- **Pydantic**
- **JWT (JSON Web Tokens)**
- **Argon2 (password hashing)**
- **Uvicorn**
- **Python 3.10+**

---

## 📂 Estructura del proyecto
```code
app/
│
├── main.py
├── database.py
│
├── models/
│ └── user_model.py
│
├── schemas/
│ └── user_schema.py
│
├── repositories/
│ └── user_repository.py
│
├── services/
│ └── auth_service.py
│
├── auth/
│ ├── jwt_handler.py
│ ├── password_handler.py
│ └── auth_dependencies.py
│
├── routers/
│ └── auth_router.py
│
├── commands/
│ └── seed_command.py
│
└── config/
└── settings.py
```

---

## ⚙️ Configuración del entorno

### 1️⃣ Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar dependencias

pip install -r requirements.txt

### 3️⃣ Variables de entorno

Crear un archivo .env en la raíz del proyecto:

```code
# DATABASE
DATABASE_URL=sqlite:///./database.db

# JWT
JWT_SECRET_KEY=super-secret-key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
```

⚠️ Nunca subir el archivo .env al repositorio

▶️ Ejecutar la aplicación
uvicorn app.main:app --reload


📍 La API estará disponible en:

📍 La API estará disponible en:

http://localhost:8000

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc