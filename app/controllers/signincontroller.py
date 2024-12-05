from app.database import db  # Import your database client

def signin_user_or_freelancer(email: str, password: str):
    # Check if the user exists in the "users" collection
    user = db.users.find_one({"email": email})
    if user:
        # Verify the password here (you can use bcrypt or any hashing method)
        return user

    # Check if the user exists in the "freelancers" collection
    freelancer = db.freelancers.find_one({"email": email})
    if freelancer:
        # Verify the password here (you can use bcrypt or any hashing method)
        return freelancer

    # Raise an error if neither a user nor a freelancer is found
    raise ValueError("Invalid email or password")
