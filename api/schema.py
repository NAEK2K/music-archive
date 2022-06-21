"""
Schemas for data validation and structure.
"""
from pydantic import BaseModel


class UserBase(BaseModel):
    """
    Base user schema.
    """

    email: str


class UserCreate(UserBase):
    """
    Create user schema.
    """

    name: str
    password: str


class User(UserBase):
    """
    ORM user schema.
    """

    id: int
    name: str

    class Config:
        """
        Pydantic config.
        """

        orm_mode = True


class BandBase(BaseModel):
    """
    Base band schema.
    """

    name: str


class Band(BandBase):
    """
    ORM band schema.
    """

    id: int

    class Config:
        """
        Pydantic config.
        """

        orm_mode = True
