from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db, Base, engine
from app.models.destino import Destino

# Crear tablas
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/destinos", tags=["Destinos"])

# Listar destinos
@router.get("/")
def listar_destinos(db: Session = Depends(get_db)):
    return db.query(Destino).all()

# Crear destino
@router.post("/")
def crear_destino(nombre: str, localidad: str, categoria: str, costo: str, horarios: str, db: Session = Depends(get_db)):
    nuevo = Destino(nombre=nombre, localidad=localidad, categoria=categoria, costo=costo, horarios=horarios)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Obtener destino por ID
@router.get("/{id}")
def obtener_destino(id: int, db: Session = Depends(get_db)):
    destino = db.query(Destino).filter(Destino.id == id).first()
    if not destino:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    return destino

# Actualizar destino
@router.put("/{id}")
def actualizar_destino(id: int, nombre: str, localidad: str, categoria: str, costo: str, horarios: str, db: Session = Depends(get_db)):
    destino = db.query(Destino).filter(Destino.id == id).first()
    if not destino:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    destino.nombre = nombre
    destino.localidad = localidad
    destino.categoria = categoria
    destino.costo = costo
    destino.horarios = horarios
    db.commit()
    db.refresh(destino)
    return destino

# Eliminar destino
@router.delete("/{id}")
def eliminar_destino(id: int, db: Session = Depends(get_db)):
    destino = db.query(Destino).filter(Destino.id == id).first()
    if not destino:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    db.delete(destino)
    db.commit()
    return {"mensaje": "Destino eliminado correctamente"}
