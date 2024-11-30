from fastapi import FastAPI
from app.routes.endpoint import endpoints
from app.routes.statsRoute import stats_router

app = FastAPI()

# Include the router from the routes file
app.include_router(endpoints)
app.include_router(stats_router , prefix="/api")
