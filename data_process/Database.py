from pymongo import MongoClient

class Database():

  def __init__(self):
    self.client = MongoClient('localhost', 27017)
    self.db = self.client['market']
    pass

  def write_to_collection(self, name, val):
    collection = self.db[name]
    collection.insert_one(val)
  