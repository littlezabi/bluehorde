import pymongo

if __name__ == '__main__':
    from modals import *
else:
    from .modals import *


class Mongo:
    def __init__(self, collection='mobile_devices'):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db_name = 'bluehorde'
        self.db = self.client[self.db_name]
        self.collection = collection
        self.modal = Modal(self.db, self.collection)

    def _list(self):
        _list = self.client.list_database_names()
        return _list

    def isExist(self, db):
        if db in self._list():
            return True
        else:
            return False


if __name__ == '__main__':
    # mongo = Mongo('URLs_list')
    mongo = Mongo()
    mdm = mongo.modal
    # k = mongo._list()
    # print('col: ', k)
    # k = mongo.isExist(mongo.db_name)
    # k = mdm.insert_one({
    #     'url_id': 1,
    #     'url_name': 'hello-world',
    #     'url': 'https:asdf',
    #     'createdAt': '2.222'
    # })
    # k = mongo.MDM().insert_one({'title': 'abc', 'desc': 'lorem ipsum'})
    # k = mdm.find({}, {'title': 1}).sort('title', -1)
    # k = mdm.delete_many()
    # k = mdm.update_many({'scrapped': True}, {
    #     '$set': {'scrapped': False}})
    i = 0
    for l in mdm.find().limit(5):
        # i += 1
        # mdm.update_one({'_id': l['_id']}, {
        #                '$set': {'id': i, 'from': 'gsmarena'}})
        print('data: ', l['slug'])
    # slug = createSlug(l['name'])
    # id = l['_id']
    # mdm.update_one({'_id': id}, {'$set': {'slug': slug}})
