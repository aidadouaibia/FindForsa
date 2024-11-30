from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    nom: str
    prenom: str
    email: str
    num_carte: str
    date_carte: str
    code_carte: str
    nom_carte: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: str
    class Config:
        orm_mode = True