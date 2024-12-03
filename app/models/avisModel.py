from pydantic import BaseModel
from typing import Optional

# Model to handle incoming review data
class AvisBase(BaseModel):
    avis: str
    id_auteur: str
    role_auteur: str

# Response Model for reviews
class AvisResponse(BaseModel):
    id_auteur: Optional[str]
    role_auteur: str
    id: str
    avis: str
    nom_complet: str  # Full name (nom + prenom)
    
    class Config:
        orm_mode = True
