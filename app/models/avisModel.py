from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
class AvisBase(BaseModel):
    avis: str
    id_auteur: str
    role_auteur: str

class AvisResponse(AvisBase):
    id: str
    class Config:
        orm_mode = True