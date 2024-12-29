<<<<<<< HEAD
from pydantic import BaseModel
from typing import Optional

# Model to handle incoming review data
=======
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
>>>>>>> friend/lil
class AvisBase(BaseModel):
    avis: str
    id_auteur: str
    role_auteur: str

<<<<<<< HEAD
# Response Model for reviews
class AvisResponse(BaseModel):
    id_auteur: Optional[str]
    role_auteur: str
    id: str
    avis: str
    nom_complet: str  # Full name (nom + prenom)
    
    class Config:
        orm_mode = True
=======
class AvisResponse(AvisBase):
    id: str
    class Config:
        orm_mode = True
>>>>>>> friend/lil
