from bson import ObjectId

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.testDb

cities_collection = db['cities']
codes_collection = db['codes']

cities = cities_collection.find()
codes = codes_collection.find()

for city in cities:
    print(city["_id"])
    cities_collection.update_one({"_id": city["_id"]}, {"$set": {"population": int(city["population"]),
                                                                  "percent_of_code_in_city": int(city["percent_of__code_in_city"]),
                                                                  "percent_of_city_in_code": int(city["percent_of_city_in_code"])}})


for code in codes:
    codes_collection.update_one({"_id": code["_id"]}, {"$set": {"id": int(code["id"]),
                                                                  "code_id": int(code["code_id"]),
                                                                  "countypop": int(code["countypop"]),
                                                                  "latitude": float(code["latitude"]),
                                                                  "longitude": float(code["longitude"])}})
