import hashlib

from pymongo import MongoClient
#from Flask import UserName


def addit(name, mail, password):
    global users
    hash_object = hashlib.sha256(password.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    if name != '' and mail != '' and password != '':
        if users.find_one({"name": name}) != None:
            print("Name is used by someone")
            # exMess="Name is used by someone"
            # return exMess
        elif users.find_one({"mail": mail}) != None:
            print("Mail is used by someone")
            # exMess = "Name is used by someone"
            # return exMess
        else:
            projList = []
            users.insert_one({"name": name, "mail": mail, "password": hex_dig, "projectsList": projList})
    else:
        print("some information isn't entered")



def checkit(name, password):
    global users

    if users.find_one({"name": name}) == None:
        print("Name is not used by anyone")
        # вывести, что нет такого юзера
    elif users.find_one({"name": name}) != None and password != '':
        hash_object = hashlib.sha256(password.encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        data = users.find_one({"name": name})
        truepassword = data["password"]
        if hex_dig == truepassword:
            print("Congrats! You've just entered!")
            return name
            # Tут вход в сайт и продолжение работы
        else:
            print("Wrong password!")
            # Тут вывести, что не тот пароль
    else:
        print('Password is not entered!')

def createTask(): #сюда передать входные - название задания, текст, т.п.
    global tasks
    global users
    global UserName

    userData = users.find_one({'name': UserName})

    #users.insert_one({"name": name, "mail": mail, "password": hex_dig})
    #tasks.insert_one({"name": name, "mail": mail, "password": hex_dig}) #как раз эти входные





client = MongoClient("localhost", 27017)
db = client.test_database

users = db.users
tasks = db.tasks
# users.insert_many([{"name": name, 'state': 'to-do'}]) #?
# for elem in users.find_one({'task': 'design', 'state': 'to-do'}):
#    print(elem)
# for elem in users.find_one({"$or": [{'task': 'design'}, {'state': 'to-do'}]}):
#    print(elem)
