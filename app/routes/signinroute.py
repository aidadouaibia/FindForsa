from fastapi import APIRouter
from pydantic import BaseModel
from app.controllers.signincontroller import signin_user_or_freelancer


user_freelancer_router = APIRouter()

class SigninRequest(BaseModel):
    email: str
    password: str


class SigninResponse(BaseModel):
    id: str
    message: str


@user_freelancer_router.post("/signin", response_model=SigninResponse)
def signin(data: SigninRequest):
    result = signin_user_or_freelancer(data.email, data.password)
    return {"id": str(result["_id"]), "message": "Signin successful"}
