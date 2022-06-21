from tkinter import W
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from database import Base

user_band_table = Table(
    "user_band",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("band_id", ForeignKey("bands.id")),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    bands = relationship("Band", secondary=user_band_table)


class Band(Base):
    __tablename__ = "bands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    collections = relationship("Collection")


class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    band_id = Column(Integer, ForeignKey("bands.id"))

    songs = relationship("Song")


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    collection_id = Column(Integer, ForeignKey("collections.id"))
