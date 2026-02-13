from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database
import models
import schema

app = FastAPI()

# Dependencia: Nos da una sesión de DB y la cierra cuando terminamos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Crypto-Tracker API v1.0"}

@app.get("/prices")
def get_prices(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Devuelve los últimos precios guardados en la base de datos.
    """
    # Query SQL: SELECT * FROM bitcoin_prices ORDER BY id DESC LIMIT 10
    prices = db.query(models.BitcoinPrice)\
               .order_by(models.BitcoinPrice.id.desc())\
               .offset(skip)\
               .limit(limit)\
               .all()
    return prices
