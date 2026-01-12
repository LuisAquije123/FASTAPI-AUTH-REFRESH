from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import auth_router
from app.commands.seed_command import run_seed


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 🔹 Startup
    Base.metadata.create_all(bind=engine)
    run_seed()
    yield
    # 🔹 Shutdown (si luego necesitas cerrar conexiones)


app = FastAPI(lifespan=lifespan)

# 🔐 CORS (OBLIGATORIO para frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Frontend (Next.js / React)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(auth_router.router)
