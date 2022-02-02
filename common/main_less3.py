import pymongo
from pymongo import MongoClient
from pymongo import errors
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)

db = client['users2401']
# db2 = client['users1_2401']
# db3 = client['users2_2401']

persons = db.persons  # РљРѕР»Р»РµРєС†РёСЏ
books = db.books  # РљРѕР»Р»РµРєС†РёСЏ

# persons.create_index([('text', pymongo.TEXT)], name='search_index', unique=True)

# doc = {"_id": 564843135186,
#        "author": "Peter2",
#        "age": 38,
#        "text": "is cool! Wildberry",
#        "tags": ['cool', 'hot', 'ice'],
#        "date": '14.06.1983'}

# try:
#     persons.insert_one(doc)
# except errors.DuplicateKeyError:
#     print(f'Р”РѕРєСѓРјРµРЅС‚ СЃ РїРѕР»РµРј {doc["_id"]} СѓР¶Рµ СЃСѓС‰РµСЃС‚РІСѓРµС‚ РІ Р±Р°Р·Рµ')

# persons.insert_many([{"author": "John",                               # Р”РѕР±Р°РІР»СЏРµРј РЅРµСЃРєРѕР»СЊРєРѕ РґРѕРєСѓРјРµРЅС‚РѕРІ РІ Р±Р°Р·Сѓ
#                "age" : 29,
#                "text": "Too bad! Strawberry",
#                "tags": 'ice',
#                "date": '04.08.1971'},
#
#                     {"_id": 123,
#                         "author": "Anna",
#                "age" : 36,
#                "title": "Hot Cool!!!",
#                "text": "easy too!",
#                "date": '26.01.1995'},
#
#                    {"author": "Jane",
#                "age" : 43,
#                "title": "Nice book",
#                "text": "Pretty text not long",
#                "date": '08.08.1975',
#                "tags":['fantastic', 'criminal']}])


# for doc in persons.find({}):
#     pprint(doc)

# for doc in persons.find({'author': 'Peter2', 'age': 36}):
#     pprint(doc)


# for doc in persons.find({'$or':
#                              [{'author': 'Peter2'},
#                               {'age': 36}
#                               ]}):
#     pprint(doc)

# for doc in persons.find({'age': {'$lte': 35}, 'author': 'Peter2'}):
#     pprint(doc)

# for doc in persons.find({'$or':
#                              [{'author': 'Peter2'},
#                               {'age': {'$lte': 35}}
#                               ]}):
#     pprint(doc)




# for doc in persons.find({'author': {'$regex': 'J'}}):
#     pprint(doc)


# result = persons.find_one({'author': 'Peter2'})
# if result:
#     print('Р’Р°СЃСЏ РЅР°Р№РґРµРЅ')
# else:
#     print('Р”РѕР±Р°РІР»СЏРµРј Р’Р°СЃСЋ')

# new_data = {
#     "author": "Andrey",
#                "age" : 28,
#                "text": "is hot!",
#                "date": '11.09.1991'}

# persons.update_one({'author': 'Peter'}, {'$set': {'phone': '84951264578'}})
# persons.update_one({'author': 'Peter2'}, {'$set': new_data})
#
# persons.replace_one({'author': 'Andrey'}, new_data)

# persons.update_one({'author': 'Peter'}, {'$unset': {'phone': ''}})
# persons.update_many()

# persons.delete_one({'author': 'Andrey'})
# persons.delete_many({})


for doc in persons.find({}):
    pprint(doc)