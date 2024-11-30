from app.database import db

def get_statistics():
    user_count = db["users"].count_documents({})
    freelancer_count = db["freelancers"].count_documents({})
    review_count = db["reviews"].count_documents({})
    project_count = db["projects"].count_documents({})
    
    return {
        "users": user_count,
        "freelancers": freelancer_count,
        "reviews": review_count,
        "projects": project_count,
    }
