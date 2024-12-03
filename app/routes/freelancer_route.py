from fastapi import APIRouter
from app.controllers.freelancercontroller import get_all_freelancers
from app.models.freelancerModel import FreelancerResponse
from typing import List

freelancer_router = APIRouter()

@freelancer_router.get("/freelancers/", response_model=List[FreelancerResponse])
def get_freelancers():
    """
    Fonction pour récupérer tous les freelancers de la collection MongoDB.
    """
    return get_all_freelancers()
