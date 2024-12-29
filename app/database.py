from pymongo import MongoClient
from app.config import DATABASE_URI, DB_NAME

<<<<<<< HEAD
client = MongoClient(DATABASE_URI)

db = client[DB_NAME]
users_collection = db["users"]
freelancers_collection = db["freelancers"]
avis_collection = db["avis"]
=======

client = MongoClient(DATABASE_URI)

db = client[DB_NAME]
>>>>>>> friend/lil
