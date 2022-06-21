"""
The FastAPI server.
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schema
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    return crud.create_user(db=db, user=user)


@app.post("/bands/", response_model=schema.Band)
def create_band(band: schema.BandBase, db: Session = Depends(get_db)):
    db_band = crud.get_band_by_name(db, name=band.name)
    if db_band:
        raise HTTPException(status_code=400, detail="Band already exists.")
    return crud.create_band(db=db, band=band)
