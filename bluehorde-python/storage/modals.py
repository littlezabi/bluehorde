class Modal:
    def __init__(self, db, collection):
        self.col = collection
        self.db = db
        self.collection = db[self.col]

    def update_many(self, filter={}, update={}):
        return self.collection.update_many(filter, update)

    def update_one(self, filter={}, update={}):
        return self.collection.update_one(filter, update)

    def delete_one(self, occ):
        self.collection.delete_one(occ)
        return 1

    def delete_many(self, obj_={}):
        return self.collection.delete_many(obj_).deleted_count

    def insert_one_(self, obj_):
        self.collection.insert_one(obj_)
        return 1

    def insert_one(self,  obj_):
        _id = self.collection.insert_one(obj_).inserted_id
        return self.collection.find_one({'_id': _id})

    def insert_many(self, arr):
        _id = self.collection.insert_many(arr).inserted_id
        return self.collection.find_one({'_id': _id})

    def find(self, occ={}, fields={}):
        return self.collection.find(occ, fields)

    def drop(self):
        self.collection.drop()
