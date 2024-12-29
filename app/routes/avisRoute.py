from fastapi import APIRouter, HTTPException
from app.controllers.avisControl import post_avis, get_avis
from app.models.avisModel import AvisBase, AvisResponse  # Ensure correct imports
from typing import List

avis_router = APIRouter()

# Route to post a review
@avis_router.post("/avis", response_model=AvisResponse)
def post_review(avis: AvisBase):
    try:
        # Post the review to the database
        avis_data = avis.dict()
        review_response = post_avis(avis_data)  # Get the full response

        # Return the review response directly
        return review_response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Route to get all reviews
@avis_router.get("/avis", response_model=List[AvisResponse])
def get_reviews():
    try:
        reviews = get_avis()  # Get all reviews
        return reviews  # Return the list of reviews directly
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
