from fastapi import APIRouter, HTTPException
from pymongo.collection import Collection
from bson import ObjectId
from app.database import db

router = APIRouter()

# Define collections
projects_collection: Collection = db["projects"]
freelancers_collection: Collection = db["freelancers"]

@router.get("/recommendations/{project_id}", tags=["Recommendations"])
async def recommend_freelancers(project_id: str, top_n: int = 5):
    # Validate Project ID
    if not ObjectId.is_valid(project_id):
        raise HTTPException(status_code=400, detail="Invalid project ID format")

    # Fetch project details
    project = projects_collection.find_one({"_id": ObjectId(project_id)})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")

    # Extract project attributes
    required_technologies = project.get("technologies", [])
    required_categories = project.get("categories", [])
    project_responsabilities = project.get("responsabilities", [])

    # Fetch all freelancers
    freelancers = freelancers_collection.find()

    # Calculate scores for each freelancer
    recommendations = []
    for freelancer in freelancers:
        score = 0

        # Match Expertise
        freelancer_expertise = freelancer.get("Expertise", "").split(", ")
        expertise_matches = [tech for tech in required_technologies if tech in freelancer_expertise]
        score += len(expertise_matches) * 3

        # Match Categories
        freelancer_categories = freelancer.get("Categories", [])
        category_matches = [cat for cat in required_categories if cat in freelancer_categories]
        score += len(category_matches) * 2

        # Match Responsibilities
        freelancer_description = freelancer.get("description", "")
        responsibility_matches = [resp for resp in project_responsabilities if resp in freelancer_description]
        score += len(responsibility_matches)

        # Match Profession
        if project.get("categories") and freelancer.get("profession").lower() in " ".join(project.get("categories")).lower():
            score += 3

        # Add freelancer to recommendations if score > 0
        if score > 0:
            recommendations.append({
                "freelancer_id": str(freelancer["_id"]),
                "name": f"{freelancer['nom']} {freelancer['prenom']}",
                "email": freelancer["email"],
                "profession": freelancer["profession"],
                "level": freelancer["level"],
                "score": score
            })

    # Sort recommendations by score
    recommendations = sorted(recommendations, key=lambda x: x["score"], reverse=True)

    # Return top-N recommendations
    return {"project_id": project_id, "recommendations": recommendations[:top_n]}
