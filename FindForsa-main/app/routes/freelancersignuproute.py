from fastapi import APIRouter, HTTPException
from app.controllers.freelancersignupcontroller import save_step1, save_step2, save_step3, save_step4
from app.models.freelancerModel import Step1, Step2, Step3, Step4 

from app.database import db
from bson import ObjectId

freelancers = db["freelancers"]

freelancer_route = APIRouter()

@freelancer_route.post("/signup/step1")
def step1(data: Step1):
    # Créer un document avec les données de la première étape
    result = freelancers.insert_one(data.dict())
    return {"id": str(result.inserted_id)}

@freelancer_route.post("/signup/step2/{freelancer_id}")
def step2(freelancer_id: str, data: Step2):
    # Valider l'ObjectId
    if not ObjectId.is_valid(freelancer_id):
        raise HTTPException(status_code=400, detail="L'ID fourni n'est pas valide")

    # Convertir en ObjectId
    freelancer_id = ObjectId(freelancer_id)

    # Mettre à jour le document
    result = freelancers.update_one(
        {"_id": freelancer_id},
        {"$set": data.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Freelancer introuvable")
    return {"message": "Étape 2 ajoutée avec succès"}



@freelancer_route.post("/signup/step3/{freelancer_id}")
def step3(freelancer_id: str, data: Step3):
    # Ajouter les données de l'étape 3
    result = freelancers.update_one(
        {"_id": ObjectId(freelancer_id)},
        {"$set": data.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Freelancer not found")
    return {"message": "Step 3 data added"}

@freelancer_route.post("/signup/step4/{freelancer_id}")

def step4(freelancer_id: str, data: Step4):
    # Ajouter les données de l'étape 4
    result = freelancers.update_one(
        {"_id": ObjectId(freelancer_id)},
        {"$set": data.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Freelancer not found")
    return {"message": "Step 4 data added"}



