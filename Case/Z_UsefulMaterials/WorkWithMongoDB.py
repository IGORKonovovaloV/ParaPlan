from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.test_database

tasks = db.tasks
tasks.insert_many([{'task': "design", 'state': 'to-do'},{'task': 'edit', 'state': 'done'},{'task': 'backend', 'state': 'done'}])
for elem in tasks.find_one({'task': 'design', 'state': 'to-do'}):
    print(elem)
for elem in tasks.find_one({"$or": [{'task': 'design'}, {'state': 'to-do'}]}):
    print(elem)