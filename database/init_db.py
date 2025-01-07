print("inocio init_db")

from pymongo import MongoClient

def init_db():
    mongo_uri = "mongodb://localhost:27017/"
    client = MongoClient(mongo_uri)
    db_name = "image_gen_app"
    db = client[db_name]
    return db

def initialize_collections(db):
    required_collections = ["profiles", "generated_images"]
    for collection in required_collections:
        if collection not in db.list_collection_names():
            db.create_collection(collection)

if __name__ == "__main__":
    db = init_db()
    initialize_collections(db)
