from fastapi import APIRouter
from app.database import db
<<<<<<< HEAD
=======

>>>>>>> friend/lil
from bson.objectid import ObjectId


endpoints = APIRouter()

@endpoints.get("/")
def home():
<<<<<<< HEAD
    users = list(db["users"].find())
    # Convert ObjectId to string for JSON serialization
    for user in users:
        user["_id"] = str(user["_id"])
    return {"message": "Welcome home", "users": users}
=======

    return {"message": "Welcome home"}
>>>>>>> friend/lil
