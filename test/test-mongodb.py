from pprint import pprint
import pymongo
import datetime
mongo_client = pymongo.MongoClient('henryzhuhr.xyz', 27017)
# pprint(mongo_client.server_info()) #判断是否连接成功
mongo_db = mongo_client['plantsmate']
mongo_collection = mongo_db['device']

# 插入单数据
info = {
    'name' : 'Zarten',
    'text' : 'Inserting a Document',
    'tags' : ['a', 'b', 'c'],
    'date' : datetime.datetime.now()
}
mongo_collection.insert_one(info)

# 插入多数据
info_1 = {
    'name' : 'Zarten_1',
    'text' : 'Inserting a Document',
    'tags' : ['a', 'b', 'c'],
    'date' : datetime.datetime.now()
}

info_2 = {
    'name' : 'Zarten_1',
    'text' : 'Inserting a Document',
    'tags' : [1, 2, 3],
    'date' : datetime.datetime.now()
}

insert_list = [info_1, info_2]
mongo_collection.insert_many(insert_list)




find_condition = {
    'name' : 'Zarten_1',
}
find_result_cursor = mongo_collection.find(find_condition)
print(find_result_cursor)
for find_result in find_result_cursor:
    print(find_result)