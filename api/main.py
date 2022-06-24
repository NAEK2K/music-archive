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

app = FastAPI(title="Music Archive")


def get_db():
    """
    DB dependency.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schema.UserCreateResponse, tags=["users"])
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    """
    Route to create a new user.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    return crud.create_user(db=db, user=user)


@app.post("/bands/", response_model=schema.BandCreateResponse, tags=["bands"])
def create_band(band: schema.BandCreate, db: Session = Depends(get_db)):
    """
    Route to create a new band.
    """
    db_band = crud.get_band_by_name(db, name=band.name)
    if db_band:
        raise HTTPException(status_code=400, detail="Band already exists.")
    return crud.create_band(db=db, band=band)


@app.post("/bands/join", response_model=schema.BandJoinResponse, tags=["bands"])
def join_band(band_join: schema.BandJoin, db: Session = Depends(get_db)):
    """
    Route to add a user to a band.
    """

    if not crud.get_user(db, user_id=band_join.user_id):
        raise HTTPException(status_code=400, detail="The user does not exist.")

    if not crud.get_band(db, band_id=band_join.band_id):
        raise HTTPException(status_code=400, detail="The band does not exist.")
    users_in_band = crud.get_band_users(db=db, band_id=band_join.band_id)
    if list(filter(lambda user: user.user_id == band_join.user_id, users_in_band)):
        raise HTTPException(status_code=400, detail="User already in this band.")

    return crud.add_user_band(db=db, band_join=band_join)
