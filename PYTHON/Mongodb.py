import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:3000/")
mydb = myclient["mydatabase"]
mycol = mydb["Songs"]
mydict = { "Name": "River", "Artist": "Eminem" }

x = mycol.insert_one(mydict)

print(mydb.list_collection_names())