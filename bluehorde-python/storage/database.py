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


categories = []


def getCateg(name):
    global categories
    categ = name.split(' ')[0]
    categ = categ.strip()
    m = 1
    if categ == '':
        categ = name.split(' ')[1]

    for c in categories:
        if c == categ:
            # print('matched ', name, categ)
            m = 0
            return
    if m:
        categories.append(categ.lower())


categories = []


def setCategory(list_, catcol, mobiles):
    item = list_['name'].split(' ')[0]
    if item == '':
        item = list_['name'].split(' ')[1]
    m = 1
    item = item.lower()
    for cat in categories:
        k = cat['category']
        if item == k:
            mobiles.update_one({'_id': list_['_id']}, {
                               '$set': {'category': k, 'cat_id': cat['_id']}})
            catcol.update_one({'_id': cat['_id']}, {'$inc': {'items': 1}})
            m = 0
            return 1
    if m:
        # categ = catcol.find({'category': item})
        # if len(list(categ)) > 0:
        #     catcol.update_one({'category': item}, {'$inc': {'items': 1}})
        # else:
        #     catcol.insert_one_({'category': item, 'items': 1, 'image': ''})
        # mobiles.update_one({'_id': list_['_id']}, {'$set': {'category': item}})
        # print('added')
        # return 1
        pass


if __name__ == '__main__':
    # mongo = Mongo('URLs_list')
    catdb = Mongo('categories')
    mobdb = Mongo()
    catcol = catdb.modal
    mobiles = mobdb.modal

    # catlist = [k for k in catcol.find({}, {'category': 1})]
    # print(catlist)

    # for k in catcol.find({}, {'_id': 0, 'category': 1, 'items': 1}):
    #     print(k)
    # i = 0
    # for k in mobiles.find({'name': 'Xiaomi Redmi Note 9 Pro (India)'}, {'_id': 0, 'name': 1, 'category': 1}):
    #     print(i, '-> ', k)
    #     i += 1
