import pymongo
from bson import json_util
import json

from config import ConfigParams
from models.space import Space

dbclient = pymongo.MongoClient(ConfigParams.MONGODB_HOST)
db = dbclient[ConfigParams.MONGODB_NAME]
spaces_collection = db["spaces"]


class DBSpaces:
    def write(self, space_offer):
        try:
            w = spaces_collection.insert_one(space_offer)
        except Exception as e:
            print("Error inserting: ", e)
            return 1

        return 0

    def find(self, space_request):
        space = Space(
            type="",
            region="",
            availability_start="",
            availability_end="",
            visitors_max=0,
            pet_friendly=False
        )
        spaces = []

        space.type = space_request["type"]
        space.region = space_request["region"]
        space.availability_start = space_request["availability_start"]
        space.availability_end = space_request["availability_end"]
        space.visitors_max = space_request["visitors_max"]
        space.pet_friendly = space_request["pet_friendly"]

        try:
            cursor = spaces_collection.find(space.dict(), { "_id": 0 })
            # remove type for a braoder search
            if cursor.count() == 0:
                new_space = space.dict()  # since Space does not allow object transformations
                del new_space["type"]
                cursor = spaces_collection.find(new_space, { "_id" :0 })

            for doc in cursor:
                json_doc = json.dumps(doc, default=json_util.default)
                spaces.append(json_doc.replace("\"", ""))

        except Exception as e:
            print("Failed to query database: ", e)
            return 1

        return spaces

    def latest(self):
        spaces = []

        cursor = spaces_collection.find({}, { "_id": 0, "owner": 0, "owner_age": 0, "telephone": 0, "email": 0 }).sort("_id", 1)
        for doc in cursor:
            json_doc = json.dumps(doc, default=json_util.default)
            spaces.append(json_doc.replace("\"", ""))

        return spaces