import pymongo
from fastapi import HTTPException
from bson.json_util import dumps

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydb"]     # Create database named mydb

collection = db["song"]
collection.drop()

collection = db["podcast"]
collection.drop()

collection = db["audiobook"]
collection.drop()


def get_instance(type, id):
    collection = db[type]

    query = { "id": id }
    try :
        result =  list(collection.find(query))
        json_ob = dumps(result)
        return json_ob
    except :
        raise HTTPException(status_code=400, detail="Delete Error")

def insert_file(type, dict_item):
    collection = db[type]
    collection.create_index('id', unique = True)

    try :
        x = collection.insert_one(dict_item)
        return str(x.inserted_id)
    except (pymongo.errors.DuplicateKeyError):
        raise HTTPException(status_code=400, detail="Duplicate Error")

def delete_instance(type, id):
    collection = db[type] # select collection.

    query = { "id": id }
    try :
        collection.delete_one(query)
    except :
        raise HTTPException(status_code=400, detail="Delete Error")

def update_instance(type, id, meta):
    collection = db[type] # select collection.

    query = { "id": id }
    newvalues = { "$set": meta }
    try :
        collection.update_one(query, newvalues)
    except :
        raise HTTPException(status_code=400, detail="Update Error")
