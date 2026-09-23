"""
Topic: Python + MongoDB
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
Covers: connection, create, read, update, delete, error handling, basic CRUD.
Install with: pip install pymongo
Credentials are read from environment variables - never hard-code them.
"""
import os

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.environ.get("DB_NAME", "python_learning")


def get_collection():
    """Connect to MongoDB and return the 'students' collection."""
    import pymongo
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db["students"]


def insert_student(name, score):
    """CREATE - insert one document."""
    collection = get_collection()
    return collection.insert_one({"name": name, "score": score})


def get_students():
    """READ - fetch all documents."""
    collection = get_collection()
    return list(collection.find())


def update_score(name, new_score):
    """UPDATE - modify a document matching a filter."""
    collection = get_collection()
    return collection.update_one({"name": name}, {"$set": {"score": new_score}})


def delete_student(name):
    """DELETE - remove a document matching a filter."""
    collection = get_collection()
    return collection.delete_one({"name": name})


if __name__ == "__main__":
    try:
        insert_student("Galih", 91)
        print(get_students())
    except ImportError:
        print("Install pymongo to run this file for real: pip install pymongo")
    except Exception as exc:  # noqa: BLE001 - top-level demo guard
        print(f"Could not connect to MongoDB (this is expected without a real DB): {exc}")

# ============================================
# PRACTICE
# ============================================
# EASY 1: Add a `find_by_name(name)` function returning one document or None.
# EASY 2: Add a `count_students()` function using collection.count_documents({}).
# EASY 3: Insert multiple students at once using insert_many().
# MEDIUM 1: Add error handling for pymongo.errors.ConnectionFailure.
# MEDIUM 2: Add a query that finds all students with score >= 80 using $gte.
#
# CHALLENGE: Build a small CLI (using input()) that lets a user add, view,
# update, and delete students via these functions.

# ============================================
# SUMMARY
# ============================================
# MongoDB stores flexible JSON-like documents; pymongo's API maps closely
# to the create/read/update/delete operations you already know from SQL.
