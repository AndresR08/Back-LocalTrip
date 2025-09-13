from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Destino(Base):
    __tablename__ = "destinos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    localidad = Column(String)
    categoria = Column(String)
    costo = Column(String)
    horarios = Column(String)
