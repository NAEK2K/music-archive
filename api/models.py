"""
Models defining the database.
"""
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from database import Base

user_band_table = Table(
    "user_band",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("band_id", ForeignKey("bands.id")),
)


class User(Base):
    """
    Users table.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    bands = relationship("Band", secondary=user_band_table)


class Band(Base):
    """
    Bands table.
    """

    __tablename__ = "bands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    collections = relationship("Collection")


class Collection(Base):
    """
    Collections table.
    """

    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    band_id = Column(Integer, ForeignKey("bands.id"))

    songs = relationship("Song")


class Song(Base):
    """
    Songs table.
    """

    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    collection_id = Column(Integer, ForeignKey("collections.id"))
