import ipaddress
from pymongo import MongoClient

client = MongoClient('lochalhost', 27018)
db = client.ips

collection = db['ip_data']

ips = collection.find().batch_size(50)
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
        start_ip_numeric = int(ipaddress.IPv4Address(i["start_ip"]))
        end_ip_numeric = int(ipaddress.IPv4Address(i["end_ip"]))
    elif start_ip_type == "IPv6" and end_ip_type == "IPv6":
        start_ip_numeric = int(ipaddress.IPv6Address(i["start_ip"]))
        end_ip_numeric = int(ipaddress.IPv6Address(i["end_ip"]))
        start_ip_numeric = str(start_ip_numeric)
        end_ip_numeric = str(end_ip_numeric)
    else:
        continue

    try:
        collection.update_one({"_id": i["_id"]}, {"$set": {"start_ip_numeric": start_ip_numeric, "end_ip_numeric": end_ip_numeric}})
    except:
        continue
    print(count)
    count = count + 1
