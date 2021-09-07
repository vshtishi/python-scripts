import firebase_admin

cred_obj = firebase_admin.credentials.Certificate(
    '/home/user/sample-database-9d2d3-firebase-adminsdk-ovdxc-b8aab56e2d.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://sample-database-9d2d3-default-rtdb.firebaseio.com/'
})

from firebase_admin import db

ref = db.reference('contacts/results/0/items')
result = ref.get()

import tabulate

header = result[0].keys()
rows = [x.values() for x in result]
# print(tabulate.tabulate(rows, header))

ref = db.reference('customers/results/0/items')
result = ref.get()

header = result[0].keys()
rows = [x.values() for x in result]
# print(tabulate.tabulate(rows, header))

ref = db.reference('products/results/0/items')
result = ref.order_by_child("list_price").get()

header = result[0].keys()
rows = [x.values() for x in result]
# print(tabulate.tabulate(rows, header))


# print(ref.order_by_child("list_price").limit_to_last(1).get())
# print(ref.order_by_child("list_price").limit_to_first(1).get())

# print(ref.order_by_child("list_price").equal_to(65.92).get())

# ref = db.reference('/locations/results/0/items/')
# result = ref.get()
# count = 0
#
# for i in result:
#     if i['city'] == "Roma":
#         ref.child(str(count)).set({})
#     count += 1


# ref = db.reference('/employees/results/0/items/')
# result = ref.get()
# count = 0
#
# for i in result:
#     if i['first_name'] == "Willow":
#         ref.child(str(count)).update({'job_title': 'Modified'})
#     count += 1

# ref = db.reference('/regions/results/0/items/')
# result = ref.get()
# count = 0
#
# ref.push().set({'region_name': 'test', 'id': 10})

# import pprint
# ref = db.reference('products/results/0/items')
# result = ref.order_by_child('list_price').start_at(60).get()
#
# pprint.pprint(result, sort_dicts=False)

import pprint
ref = db.reference('products/results/0/items')
result = ref.order_by_child('list_price').start_at(50).end_at(59).get()

pprint.pprint(result, sort_dicts=False)

