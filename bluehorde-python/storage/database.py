import pymongo
from .modals import *


class Mongo:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db_name = 'bluehorde'
        self.db = self.client[self.db_name]

    def MDM(self):
        return MOBILE_DEVICES_MODAL(self.db)

    def _list(self):
        _list = self.client.list_database_names()
        return _list

    def isExist(self, db):
        if db in self._list():
            return True
        else:
            return False


if __name__ == '__main__':
    mongo = Mongo()
    mdm = mongo.MDM()
    # k = mongo._list()
    # k = mongo.isExist(mongo.db_name)
    k = mdm.insert_one({
        'title': 'abc',
        'desc': 'lorem ipsum',
    })
    # k = mongo.MDM().insert_one({'title': 'abc', 'desc': 'lorem ipsum'})
    # k = mdm.find({}, {'title': 1}).sort('title', -1)
    # k = mdm.delete_many({'title': 'abc'})
    # k = mdm.update_many({'title': 'abc'}, {
    #     '$set': {'title': 'aa', 'desc': 'italia'}})

    # for l in mdm.find():
    #     print(l)
