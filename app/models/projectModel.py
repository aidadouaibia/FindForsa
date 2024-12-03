from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

class ProjectBase(BaseModel):
    titre: str
    description: str
    budget: str
    duree: str
    technologies: List[str]
    responsabilities: List[str]
    specifications: Optional[List[str]] = None
    contact: Optional[str] = None
    id_user: str
    categories: List[str]

class ProjectResponse(ProjectBase):
    id: str  # The id is a string now, since we converted ObjectId to string
    class Config:
        orm_mode = True