from fastapi import APIRouter
from app.database import db

from bson.objectid import ObjectId


endpoints = APIRouter()

@endpoints.get("/")
def home():

    return {"message": "Welcome home"}
