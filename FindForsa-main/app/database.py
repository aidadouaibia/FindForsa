from pymongo import MongoClient
from app.config import DATABASE_URI, DB_NAME


client = MongoClient(DATABASE_URI)

db = client[DB_NAME]