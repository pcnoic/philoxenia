import pymongo
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
        space = Space()
        spaces = []

        for space_type in space_request.types:
            space.type = space_type
            for space_region in space_request.regions:
                space.region = space_region
                space.availability_start = space_request.availability_start
                space.availability_end = space_request.availability_end
                space.visitors_min = space_request.visitors_min
                space.visitors_max = space_request.visitors_max
                space.pet_friendly = space_request.pet_friendly

                try:
                    doc = spaces_collection.find(space)
                    if doc is None:
                        space.pop('type')
                        doc = spaces_collection.find(space)
                        if doc is None:
                            break
                except Exception as e:
                    print("Failed to query database: ", e)
                    return 1
                
        return spaces

    def latest(self):
        space = Space()
        spaces = []

        docs = spaces_collection.find().sort({x:1})

