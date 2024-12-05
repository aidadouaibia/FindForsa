from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from app.models.projectModel import ProjectResponse
from app.database import db  # Import the database connection

get_project_router = APIRouter()

@get_project_router.get("/projects/", response_model=list[ProjectResponse])
def get_projects():
    """
    Function to retrieve all projects from the MongoDB collection.
    """
    try:
        # Retrieve all projects from the MongoDB collection
        projects = list(db["projects"].find())

        # Convert ObjectId fields to strings and format the results
        for project in projects:
            project["id"] = str(project["_id"])  # Convert _id to string
            del project["_id"]  # Remove the MongoDB-specific _id field
            
            # Convert id_user to string if it exists and is an ObjectId
            if "id_user" in project and isinstance(project["id_user"], ObjectId):
                project["id_user"] = str(project["id_user"])

        # Return the formatted list of projects
        return projects

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving projects: {str(e)}"
        )



### get project by id:
@get_project_router.get("/projects/{project_id}", response_model=ProjectResponse)

def get_project_by_id(project_id: str):
    """
    Function to retrieve a single project by its ID.
    """
    try:
        # Validate the ObjectId
        if not ObjectId.is_valid(project_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid project ID format"
            )

        # Retrieve the project from the MongoDB collection
        project = db["projects"].find_one({"_id": ObjectId(project_id)})

        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )

        # Convert ObjectId fields to strings
        project["id"] = str(project["_id"])  # Convert the main _id
        del project["_id"]

        # Convert `id_user` field to string if it exists
        if "id_user" in project and isinstance(project["id_user"], ObjectId):
            project["id_user"] = str(project["id_user"])

        # Return the project as a response model
        return project

    except HTTPException:
        raise  # Re-raise HTTP exceptions
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving project: {str(e)}"
        )