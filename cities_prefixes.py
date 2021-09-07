from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.testDb

cities_collection = db['cities']
codes_collection = db['codes']

cities = cities_collection.find()

for city in cities:
    prefixes = []
    matches = []
    matches = codes_collection.find({"city_name": {"$regex": city["city"], "$options": "i"},
                                      "county": {"$regex": city["county"], "$options": "i"},
                                      "state": {"$regex": city["state"], "$options": "i"}})

    for match in matches:
        prefixes.append(match["npanxx"])

    cities_collection.update_one({"_id": city["_id"]}, {"$set": {"prefixes": prefixes}})
