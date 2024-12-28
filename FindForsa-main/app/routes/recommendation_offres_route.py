from bson import ObjectId
from fastapi import APIRouter, HTTPException
from app.database import db

router = APIRouter()

@router.get("/recommendations/matching/{freelancer_id}", tags=["Recommendations"])
async def matching_recommendations(freelancer_id: str, top_n: int = 10):
    # Validate ObjectId
    if not ObjectId.is_valid(freelancer_id):
        raise HTTPException(status_code=400, detail="Invalid freelancer ID format")

    # Fetch freelancer details
    freelancer = db.freelancers.find_one({"_id": ObjectId(freelancer_id)})
    if not freelancer:
        raise HTTPException(status_code=404, detail=f"Freelancer not found with ID: {freelancer_id}")

    freelancer_profession = freelancer.get("profession")
    freelancer_categories = freelancer.get("Categories", [])
    freelancer_expertise = freelancer.get("Expertise", "").split(", ")
    freelancer_level = freelancer.get("level", "Beginner").lower()
    freelancer_description = freelancer.get("description", "")

    # Fetch all projects
    projects = db.projects.find()
    recommendations = []

    # Calculate scores
    for project in projects:
        score = 0

        # Profession Match
        if freelancer_profession in project.get("categories", []):
            score += 3

        # Category Match
        if any(category in freelancer_categories for category in project.get("categories", [])):
            score += 2

        # Expertise Match
        if any(tech in freelancer_expertise for tech in project.get("technologies", [])):
            score += 2 * len([tech for tech in project.get("technologies", []) if tech in freelancer_expertise])

        # Responsibilities Match
        if any(resp in freelancer_description for resp in project.get("responsabilities", [])):
            score += 1

        # Level Match (Optional, adjust based on logic)
        if freelancer_level == "junior" and "simple" in project.get("description", "").lower():
            score += 1
        elif freelancer_level == "expert" and "complex" in project.get("description", "").lower():
            score += 1

        # Add project to recommendations if score > 0
        if score > 0:
            recommendations.append({
                "title": project["titre"],
                "description": project["description"],
                "categories": project["categories"],
                "technologies": project["technologies"],
                "responsabilities": project["responsabilities"],
                "score": score
            })

    # Sort recommendations by score
    recommendations = sorted(recommendations, key=lambda x: x["score"], reverse=True)

    # Return top N recommendations
    return {"freelancer_id": freelancer_id, "recommendations": recommendations[:top_n]}
