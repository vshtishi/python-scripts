from pymongo import MongoClient
from tqdm import tqdm

client = MongoClient('localhost', 27017)
db = client.udata

collection = db['business_data']

businesses = collection.find()
total_count = collection.count_documents({})

count = 0

for business in tqdm(businesses, total=total_count):
    if business['Toll_Free_Number'].isspace() or business['Toll_Free_Number'] == "":
        count = count + 1

print("Blank Phones: " + str(count))
