from fastapi import APIRouter
from app.controllers.statsControl import get_statistics

stats_router = APIRouter()

@stats_router.get("/stats")
def fetch_statistics():
    stats = get_statistics()
    return {"message": "Statistics fetched successfully", "data": stats}
