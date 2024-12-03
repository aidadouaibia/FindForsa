from bson import ObjectId
from app.database import db
from app.models.freelancerModel import FreelancerResponse
from fastapi import HTTPException, status
from typing import List

def get_all_freelancers() -> List[FreelancerResponse]:
    try:
        # Récupérer tous les freelancers de la collection MongoDB
        freelancers = list(db["freelancers"].find())

        # Formater les résultats
        for freelancer in freelancers:
            freelancer["id"] = str(freelancer["_id"])  # Convertir _id en string
            del freelancer["_id"]  # Supprimer le champ _id

            # Convertir num_carte et autres ObjectId en string si nécessaire
            if "num_carte" in freelancer:
                freelancer["num_carte"] = str(freelancer["num_carte"])

        return freelancers

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving freelancers: {str(e)}"
        )