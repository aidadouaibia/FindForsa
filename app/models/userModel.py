<<<<<<< HEAD
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    nom: str
    prenom: str
    email: str
    num_carte: str
    date_carte: str
=======
from pydantic import BaseModel, EmailStr, Field
import bcrypt

class UserBase(BaseModel):
    nom: str
    prenom: str = Field(..., min_length=2, max_length=50)
    email: EmailStr  # Validation automatique des adresses e-mail
    num_carte: str
    date_carte: str 
>>>>>>> friend/lil
    code_carte: str
    nom_carte: str

class UserCreate(UserBase):
    password: str

<<<<<<< HEAD
class UserResponse(UserBase):
    id: str
    class Config:
        orm_mode = True
=======
class UserResponse(BaseModel):
    id: str
    email: str
    
class UserSignUp(BaseModel):
    nom: str
    prenom: str
    email: str
    password: str

class UserSignIn(BaseModel):
    email: str
    password: str    
>>>>>>> friend/lil
