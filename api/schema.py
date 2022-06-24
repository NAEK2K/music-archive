"""
Schemas for data validation and structure.
"""
from pydantic import BaseModel


class UserCreate(BaseModel):
    """
    Create user schema.
    """

    name: str
    email: str
    password: str


class UserCreateResponse(BaseModel):
    """
    Create user response schema.
    """

    id: int
    name: str
    email: str

    class Config:
        """
        Config
        """

        orm_mode = True


class BandCreate(BaseModel):
    """
    Create band schema.
    """

    name: str


class BandCreateResponse(BaseModel):
    """
    Create band response schema.
    """

    id: int
    name: str

    class Config:
        """
        Config
        """

        orm_mode = True


class BandJoin(BaseModel):
    """
    Join band schema.
    """

    band_id: int
    user_id: int


class BandJoinResponse(BaseModel):
    """
    Join band response schema.
    """

    band_id: int
    user_id: int

    class Config:
        """
        Config
        """

        orm_mode = True
