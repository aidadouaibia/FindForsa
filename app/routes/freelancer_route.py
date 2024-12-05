from fastapi import APIRouter, HTTPException 
from app.models.freelancerModel import FreelancerResponse
from typing import List
from app.database import db
from datetime import datetime 
from bson import ObjectId


freelancer_router = APIRouter()
freelancers_collection = db["freelancers"]


@freelancer_router.get("/freelancers/", response_model=List[FreelancerResponse])



async def get_all_freelancers():
    try:
        # Fetch freelancers from MongoDB
        freelancers_cursor = freelancers_collection.find()

        # Convert cursor to list
        freelancers = list(freelancers_cursor)

        # Ensure date_carte is in the correct format and convert ObjectId to string for _id
        for freelancer in freelancers:
            # Ensure date_carte is a string
            if isinstance(freelancer.get("date_carte"), str):
                try:
                    # Optional: Check if the date is in the correct format
                    datetime.strptime(freelancer["date_carte"], "%d/%m/%Y")
                except ValueError:
                    raise ValueError(f"Invalid date_carte format: {freelancer.get('date_carte')}")
            else:
                raise ValueError(f"Invalid date_carte value type: {type(freelancer.get('date_carte'))}")

            # Convert ObjectId to string for _id
            freelancer["_id"] = str(freelancer["_id"])

        # Return the response after validating the freelancers
        return [FreelancerResponse(**freelancer) for freelancer in freelancers]

    except Exception as e:
        print(f"Error: {e}")  # Debugging print
        raise HTTPException(status_code=400, detail=f"Error retrieving freelancers: {e}")





##get a freelancer by id :


@freelancer_router.get("/freelancers/{freelancer_id}", response_model=FreelancerResponse)
async def get_freelancer_by_id(freelancer_id: str):
    """
    Fetch a freelancer by their ID from the database.
    """
    try:
        # Vérifiez si l'ID est valide
        if not ObjectId.is_valid(freelancer_id):
            raise HTTPException(status_code=400, detail="Invalid freelancer ID format")

        # Recherche dans la collection MongoDB
        freelancer = freelancers_collection.find_one({"_id": ObjectId(freelancer_id)})

        if not freelancer:
            raise HTTPException(status_code=404, detail="Freelancer not found")

        # Validation et conversion des champs nécessaires
        if isinstance(freelancer.get("date_carte"), str):
            try:
                datetime.strptime(freelancer["date_carte"], "%d/%m/%Y")
            except ValueError:
                raise ValueError(f"Invalid date_carte format: {freelancer.get('date_carte')}")
        else:
            raise ValueError(f"Invalid date_carte value type: {type(freelancer.get('date_carte'))}")

        # Convertir l'ObjectId en chaîne pour le champ `_id`
        freelancer["_id"] = str(freelancer["_id"])

        # Retourner la réponse sous forme du modèle FreelancerResponse
        return FreelancerResponse(**freelancer)

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"Error: {e}")  # Debugging print
        raise HTTPException(status_code=500, detail=f"Error retrieving freelancer: {e}")      