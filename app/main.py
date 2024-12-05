from fastapi import FastAPI
from app.routes.endpoint import endpoints
from app.routes.statsRoute import stats_router
from app.routes.usersignuproute import user_router
from app.routes.freelancersignuproute import freelancer_route as freelancer_signup_router
from app.routes.addproject_route import project_router
from app.routes.projectroute import get_project_router
from app.routes.freelancer_route import freelancer_router
from app.routes.signinroute import user_freelancer_router
# Inclure le routeur

app = FastAPI()

# Include the router from the routes file
app.include_router(endpoints)
app.include_router(stats_router , prefix="/api")
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(freelancer_signup_router, prefix="/freelancers", tags=["Freelancers"])
app.include_router(project_router, prefix="/projects", tags=["projects"])
app.include_router(get_project_router, prefix="/projects", tags=["projects"])
app.include_router(get_project_router, prefix="/api", tags=["Projects"])
app.include_router(freelancer_router, prefix="/freelancers", tags=["Freelancers"])
app.include_router(user_freelancer_router, prefix="/auth", tags=["Authentication"])