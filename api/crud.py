"""
CRUD functions for the server.
"""

from sqlalchemy.orm import Session
from passlib.hash import sha512_crypt

import models
import schema


def get_user(db: Session, user_id: int):
    """
    Get user by ID.
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    Get user by email.
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_name(db: Session, name: str):
    """
    Get user by email.
    """
    return db.query(models.User).filter(models.User.name == name).first()


def create_user(db: Session, user: schema.UserCreate):
    """
    Create a new user.
    """
    password = sha512_crypt.hash(user.password, rounds=200000)
    db_user = models.User(email=user.email, name=user.name, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_band(db: Session, band_id: int):
    """
    Get band by ID.
    """
    return db.query(models.Band).filter(models.Band.id == band_id).first()


def get_band_by_name(db: Session, name: str):
    """
    Get band by name.
    """
    return db.query(models.Band).filter(models.Band.name == name).first()


def create_band(db: Session, band: schema.BandCreate):
    """
    Create a new band.
    """
    db_band = models.Band(name=band.name)
    db.add(db_band)
    db.commit()
    db.refresh(db_band)
    return db_band


def get_band_users(db: Session, band_id: int):
    """
    Get the users of a band.
    """
    return (
        db.query(models.user_band_table)
        .filter(models.user_band_table.c.band_id == band_id)
        .all()
    )


def add_user_band(db: Session, band_join: schema.BandJoin):
    """
    Add a user to a band.
    """
    user_band_insert = models.user_band_table.insert().values(
        user_id=band_join.user_id, band_id=band_join.band_id
    )
    db.execute(user_band_insert)
    db.commit()
    return band_join
