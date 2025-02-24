from fastapi import FastAPI
from app.routers import membros, cargos, auth, meal, dizimos, ofertas
from app.database import engine
from app.models import Base
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Igreja", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(membros.router)
app.include_router(cargos.router)
app.include_router(auth.router)
app.include_router(meal.router)
app.include_router(dizimos.router)
app.include_router(ofertas.router)