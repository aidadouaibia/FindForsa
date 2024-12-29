# app/routes/usersignuproute.py
from fastapi import APIRouter, HTTPException, status
<<<<<<< HEAD
from pydantic import BaseModel
from app.models.userModel import *
from app.controllers.usersignupController import create_user
from app.models.userModel import UserSignIn
from app.controllers.usersignincontroller import verify_user
=======
from app.models.userModel import *
from app.controllers.usersignupController import create_user


>>>>>>> friend/lil
# Création d'un routeur
user_router = APIRouter()



@user_router.post("/signup", response_model=UserSignUp)
<<<<<<< HEAD
=======
@user_router.post("/signup", response_model=UserResponse)
>>>>>>> friend/lil
async def signup_user(user: UserSignUp):
    try:
        # Appel à la fonction du contrôleur pour créer l'utilisateur
        new_user = await create_user(user)  # Attendre la fonction asynchrone
        return new_user  # Retourner la réponse de création
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
<<<<<<< HEAD
        )
    





@user_router.post("/signin")

async def signin(credentials: UserSignIn):
    try:
        user_data = await verify_user(credentials)
        return user_data  # Retourne une réponse JSON
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
=======
        )
>>>>>>> friend/lil
