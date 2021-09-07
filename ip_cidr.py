import ipaddress
import math

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.ips

collection = db['ips']

ips = collection.find()
count = 0


def validIPAddress(IP: str) -> str:
    try:
        return "IPv4" if type(ipaddress.ip_address(IP)) is ipaddress.IPv4Address else "IPv6"
    except ValueError:
        return "Invalid"


for i in ips:
    start_ip_type = validIPAddress(i["start_ip"])
    end_ip_type = validIPAddress(i["end_ip"])
    if start_ip_type == "IPv4" and end_ip_type == "IPv4":
        cidr = 32 - math.log((i["end_ip_numeric"] - i["start_ip_numeric"]) + 1, 2)
    elif start_ip_type == "IPv6" and end_ip_type == "IPv6":
        cidr = 64 - math.log((int(i["end_ip_numeric"]) - int(i["start_ip_numeric"])) / pow(2, 64), 2)
    else:
        continue

    try:
        collection.update_one({"_id": i["_id"]}, {"$set": {"cidr": cidr}})
    except:
        continue

    print(count)
    count = count + 1
