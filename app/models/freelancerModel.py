from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
class FreelancerBase(BaseModel):
    nom: str
    prenom: str
    email: str
    profession: str
    level: str
    description: str
    Github: str
    Linkedin: str
    Dribble: str
    Behance: str
    Expertise: str
    Categories: List[str]
    num_carte: str
    date_carte: str
    code_carte: str
    nom_carte: str

class FreelancerCreate(FreelancerBase):
    password: str

class FreelancerResponse(FreelancerBase):
    id: str
    class Config:
        orm_mode = True