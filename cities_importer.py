import os
path  = os.environ['path']

import numpy as np
import pandas as pd
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.testDb

collection = db['cities']
a_codes_collection = db['a_codes']

pd.set_option('display.max_rows', None)

count = 0
list = []
df = pd.DataFrame(list, columns=['a_codes', 'city', 'state', 'percent_of_code_in_city',
                                 'percent_of_city_in_code', 'city_fips', 'population'])

import csv

with open(path, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if count == 0:
            count += 1
            continue

        query = np.where((df['city'] == row[1]) & (df['state'] == row[2]) & (df['city_fips'] == row[5]))

        if len(query[0] > 0):
            if row[0] not in df.at[query[0][0], 'a_codes']:
                df.at[query[0][0], 'a_codes'].append(row[0])
            continue

        list = [[[row[0]], row[1], row[2], row[3], row[4], row[5], row[6]]]
        df2 = pd.DataFrame(list, columns=['a_codes', 'city', 'state', 'percent_of_code_in_city',
                                          'percent_of_city_in_code', 'city_fips', 'population'])
        df = df.append(df2, ignore_index=True)

for row in df.itertuples(index=True, name='Pandas'):
    codes = []
    for code in row.a_codes:
        match = a_codes_collection.find_one({"a_code": code})
        if match is None:
            codes.append(code)
        else:
            codes.append(match['_id'])

    new_entry = {
        "a_codes": codes,
        "city": row.city,
        "state": row.state,
        "percent_of_code_in_city": row.percent_of_code_in_city,
        "percent_of_city_in_code": row.percent_of_city_in_code,
        "city_fips": row.city_fips,
        "population": row.population
    }
    collection.insert_one(new_entry)
