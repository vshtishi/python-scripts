import requests
import os
batchsize = 1000
total = 5000
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient['test']
mycol = mydb["ut"]
apiUrl = os.environ['API_URL']

count = 1
for i in range(0, total, batchsize):
    res = requests.get(apiUrl + str(i) + "&size=" + str(batchsize))
    response = res.json()

    import pandas

    elastic_docs = response["hits"]["hits"]

    docs = pandas.DataFrame()
    doc_list = []
    for num, doc in enumerate(elastic_docs):
        source_data = doc["_source"]
        doc_list.append(source_data.copy())

    mycol.insert_many(doc_list)
    print('Inserted batch ' + str(count))
    count = count + 1


mycol.update_many({}, {'$unset': {"created_at": 1}})
