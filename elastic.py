import json
import pymongo
import os
path  = os.environ['path']
data = [json.loads(line) for line in open(path, 'r')]

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient['test']
mycol = mydb["ut"]

for item in data:
    for key, value in item.items():
        if key == '_source':
            print(value['created_at'])
            mycol.insert_one(value)


