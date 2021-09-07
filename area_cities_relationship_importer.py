from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.testDb

cities_collection = db['cities']
codes_collection = db['a_codes']

codes = codes_collection.find()

for code in codes:
    cities = []
    matches = cities_collection.find({"a_codes": code['_id']})
    for match in matches:
        cities.append(match['_id'])

    codes_collection.update_one({"_id": code["_id"]}, {"$set": {"cities": cities}})
