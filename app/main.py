from fastapi import FastAPI
from app.routers import destinos

app = FastAPI(title="Back-LocalTrip API")

# Rutas
app.include_router(destinos.router)

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de LocalTrip 🚀"}
