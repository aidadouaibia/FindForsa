
from app.routes.usersignuproute import UserSignUp
from app.database import db
import bcrypt

async def create_user(user_data: UserSignUp):
    try:
        # Conversion en dictionnaire
        user_dict = user_data.dict()

        # Hachage du mot de passe
        user_dict['password'] = bcrypt.hashpw(user_dict['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Insertion dans la base de données MongoDB
        result = db.users.insert_one(user_dict)

        # Retourner l'ID généré avec les autres données utilisateur
        return {
            "id": str(result.inserted_id),  # Extraire l'ID inséré
            "email": user_dict['email'],   # Inclure d'autres champs nécessaires
        }
    except Exception as e:
        raise ValueError(f"Erreur lors de la création de l'utilisateur : {e}")