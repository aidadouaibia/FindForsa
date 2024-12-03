from app.database import db
from bson import ObjectId

def get_projects_by_category(category):
    try:
        if isinstance(category, str):
            category = [category]

        projects_cursor = db.projects.find({"categories": {"$in": category}})

        projects = []
        for project in projects_cursor:
            project["_id"] = str(project["_id"])  # Convert ObjectId to string
            project["id_user"] = str(project["id_user"])  # Convert id_user (ObjectId) to string
            projects.append(project)

        return projects
    except Exception as e:
        raise ValueError(f"Erreur lors de la récupération des projets : {e}")