from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional



class Step1(BaseModel):
    nom: str
    prenom: str
    email: str
    password: str

class Step2(BaseModel):
    profession: str
    level: str
    description: str

class Step3(BaseModel):
    Github: Optional[str] = None
    Linkedin: Optional[str] = None
    Dribble: Optional[str] = None
    Behance: Optional[str] = None
    Expertise: str
    Categories: List[str]

class Step4(BaseModel):
    num_carte: str
    date_carte: str
    code_carte: str
    nom_carte: str


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

class FreelancerStep1(FreelancerBase):
    password: str

class FreelancerResponse(FreelancerBase):
    _id: str
    class Config:
        orm_mode = True

class SigninRequest(BaseModel):
    email: str
    password: str        