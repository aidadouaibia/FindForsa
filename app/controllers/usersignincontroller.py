from app.models.userModel import UserSignIn
from app.database import db
import bcrypt
import asyncio

async def verify_user(credentials: UserSignIn):
    try:
        # Recherche de l'utilisateur par email dans un thread
        user = await asyncio.to_thread(db.users.find_one, {"email": credentials.email})

        if user is None:
            raise ValueError("Utilisateur non trouvé")

        if not bcrypt.checkpw(credentials.password.encode('utf-8'), user['password'].encode('utf-8')):
           raise ValueError("Mot de passe incorrect")
        
        # Retourner un dictionnaire JSON-serializable
        return {
           
            "id": str(user['_id']),
            

        }
    except Exception as e:
        raise ValueError(f"Erreur lors de la connexion de l'utilisateur : {e}")
