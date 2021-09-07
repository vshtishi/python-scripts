from pymongo import MongoClient
import os
path = os.environ['path']

client = MongoClient('localhost', 27017)
db = client.testDb

collection = db['codes']

count = 0
import csv

with open(path, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if count == 0:
            count = 1
            continue

        new_entry = {
            "state": row[0],
            "a_code": row[1],
            "operating-company-number": row[3],
            "operating-company-name": row[4],
            "rate-center": row[5]
        }
        collection.insert_one(new_entry)
