# app/routes/usersignuproute.py
from fastapi import APIRouter, HTTPException, status
from app.models.userModel import *
from app.controllers.usersignupController import create_user


# Création d'un routeur
user_router = APIRouter()



@user_router.post("/signup", response_model=UserSignUp)
@user_router.post("/signup", response_model=UserResponse)
async def signup_user(user: UserSignUp):
    try:
        # Appel à la fonction du contrôleur pour créer l'utilisateur
        new_user = await create_user(user)  # Attendre la fonction asynchrone
        return new_user  # Retourner la réponse de création
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )