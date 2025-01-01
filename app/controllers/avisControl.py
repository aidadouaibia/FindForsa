from app.database import avis_collection, users_collection, freelancers_collection
from bson import ObjectId
from app.models.avisModel import AvisResponse
from fastapi import HTTPException
# Function to post a review
def post_avis(avis_data: dict):
    """
    Post a review to the database.
    
    :param avis_data: A dictionary with the review data.
    :return: The inserted review ID.
    """
    # Validate role (either user or freelancer)
    if avis_data["role_auteur"] not in ["user", "freelancer"]:
        raise ValueError("Invalid role. It must be 'user' or 'freelancer'.")

    # Insert the review document into the collection
    result = avis_collection.insert_one(avis_data)
    
    # Fetch the inserted review by its ID
    inserted_review = avis_collection.find_one({"_id": result.inserted_id})
    
    # Get the author's details based on the role
    if inserted_review["role_auteur"] == "user":
        author = users_collection.find_one({"_id": ObjectId(inserted_review["id_auteur"])})
    else:
        author = freelancers_collection.find_one({"_id": ObjectId(inserted_review["id_auteur"])})
    
    # Ensure 'nom_complet' is properly populated
    nom_complet = f"{author.get('nom', '')} {author.get('prenom', '')}"

    # Return the response in the format expected by the `AvisResponse` model
    response = AvisResponse(
        id=str(inserted_review["_id"]),  # Ensure 'id' is present
        avis=inserted_review["avis"],    # Ensure 'avis' is present
        role_auteur=inserted_review["role_auteur"],  # Ensure 'role_auteur' is present
        id_auteur=inserted_review["id_auteur"],  # Optional, you can remove if not needed
        nom_complet=nom_complet  # Ensure 'nom_complet' is properly set
    )

    return response




def get_avis():
    reviews = avis_collection.find()
    reviews_list = []

    for review in reviews:
        try:
            author_id = review.get("id_auteur")
            if author_id and ObjectId.is_valid(author_id):
                author = freelancers_collection.find_one({"_id": ObjectId(author_id)})
                nom_complet = f"{author.get('nom', '')} {author.get('prenom', '')}" if author else "Unknown Author"
            else:
                nom_complet = "No Author ID"

            # Append review data matching the expected schema
            reviews_list.append({
                "id_auteur": str(review.get("id_auteur", "")),
                "role_auteur": review.get("role_auteur", ""),
                "id": str(review.get("_id", "")),
                "avis": review.get("avis", ""),
                "nom_complet": nom_complet,
            })

        except Exception as e:
            print(f"Error processing review: {e}")

    # Ensure the response is a list
    if not isinstance(reviews_list, list):
        raise HTTPException(status_code=500, detail="Response must be a list.")

    return reviews_list