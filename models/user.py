"""
User Model - 3 Level Role Based Auth
Author: Gattineni Neha
Roles: Admin | Staff | User
"""

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(db, data):
    user = {
        "name": data.get("name"),
        "email": data.get("email"),
        "password": generate_password_hash(data.get("password")),
        "role": data.get("role", "User"),
        "is_active": True,
        "created_at": datetime.utcnow()
    }
    return db.users.insert_one(user)

def get_user_by_email(db, email):
    return db.users.find_one({"email": email})

def verify_password(stored_hash, password):
    return check_password_hash(stored_hash, password)

def is_admin(user):
    return user.get("role") == "Admin"

def is_staff(user):
    return user.get("role") == "Staff"
