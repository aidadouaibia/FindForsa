from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from pymongo.collection import Collection
from app.models.projectModel import ProjectBase, ProjectResponse
from app.database import db  # Import the database connection

project_router = APIRouter()

@project_router.post("/projects/", response_model=ProjectResponse)

def create_project(project: ProjectBase):
    """
    Function to create a project in the MongoDB collection.
    """
    try:
        # Convert the Pydantic model to a dictionary
        project_data = project.dict()

        # Insert the data into the MongoDB collection
        result = db["projects"].insert_one(project_data)

        # Retrieve the inserted ID and add it to the project data
        project_data["id"] = str(result.inserted_id)

        # Return the project response model
        return ProjectResponse(**project_data)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating project: {str(e)}"
        )