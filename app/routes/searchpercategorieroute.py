from fastapi import APIRouter
from app.controllers.searchpercategoriecontroller import get_projects_by_category

search_router = APIRouter()

# Route pour obtenir les projets par catégorie
search_router = APIRouter()

# Route pour obtenir les projets par catégorie
@search_router.get("/projects/category/{category}")
async def get_projects_by_category_route(category: str):
    projects = get_projects_by_category(category)
    if not projects:
        return {"message": "Aucun projet trouvé pour cette catégorie."}
    return {"projects": projects}