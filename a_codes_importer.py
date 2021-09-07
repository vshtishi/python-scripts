import os
path  = os.environ['path']

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.testDb

collection = db['a_codes']

count = 0
import csv
with open(path, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if count == 0:
           count = 1
           continue

        new_entry = {
            "area_code": row[0],
            "primary_city": row[1],
            "primary_state": row[2],
            "timezone": row[3],
        }
        collection.insert_one(new_entry)




