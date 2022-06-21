import string
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    name: str
    password: str


class User(UserBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class BandBase(BaseModel):
    name: str


class Band(BandBase):
    id: int

    class Config:
        orm_mode = True
