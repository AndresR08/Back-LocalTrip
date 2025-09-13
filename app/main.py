from fastapi import FastAPI

app = FastAPI(title="Back-LocalTrip API")

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de LocalTrip 🚀"}
