from bson import ObjectId
from app.database import db


# Étape 1 : Ajouter les informations personnelles
async def save_step1(data):
    freelancer = {
        "nom": data.nom,
        "prenom": data.prenom,
        "email": data.email,
        "password": data.password,  # Assurez-vous de hasher ce mot de passe
    }
    inserted_id = await db["freelancers"].insert_one(freelancer)
    return str(inserted_id)

# Étape 2 : Compléter le profil professionnel
async def save_step2(freelancer_id, data):
    update_data = {
        "profession": data.profession,
        "level": data.level,
        "description": data.description,
    }
    result = await db["freelancers"].update_one({"_id": ObjectId(freelancer_id)}, {"$set": update_data})
    return result.modified_count > 0

# Étape 3 : Ajouter les services
async def save_step3(freelancer_id, data):
    update_data = {
        "Categories": data.Categories,
        "Github": data.Github,
        "Linkedin": data.Linkedin,
        "Dribble": data.Dribble,
        "Behance": data.Behance,
        "Expertise": data.Expertise,
    }
    result = await db["freelancers"].update_one({"_id": ObjectId(freelancer_id)}, {"$set": update_data})
    return result.modified_count > 0

# Étape 4 : Ajouter les informations de paiement
async def save_step4(freelancer_id, data):
    update_data = {
        "num_carte": data.num_carte,
        "date_carte": data.date_carte,
        "code_carte": data.code_carte,
        "nom_carte": data.nom_carte,
    }
    result = await db["freelancers"].update_one({"_id": ObjectId(freelancer_id)}, {"$set": update_data})
    return result.modified_count > 0
