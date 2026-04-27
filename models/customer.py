"""
Customer Model
Author: Gattineni Neha
"""

from datetime import datetime

def create_customer(db, data):
    customer = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "company": data.get("company"),
        "status": data.get("status", "Lead"),
        "notes": data.get("notes", ""),
        "deals": [],
        "created_at": datetime.utcnow()
    }
    return db.customers.insert_one(customer)

def get_all_customers(db):
    return list(db.customers.find())

def get_customer_by_id(db, customer_id):
    from bson.objectid import ObjectId
    return db.customers.find_one({"_id": ObjectId(customer_id)})

def update_customer(db, customer_id, data):
    from bson.objectid import ObjectId
    return db.customers.update_one(
        {"_id": ObjectId(customer_id)},
        {"$set": data}
    )

def delete_customer(db, customer_id):
    from bson.objectid import ObjectId
    return db.customers.delete_one({"_id": ObjectId(customer_id)})
