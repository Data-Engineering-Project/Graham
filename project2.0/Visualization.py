from pymongo import MongoClient
import pymongo

class Visualization():

  def __init__(self):
    conn = MongoClient("localhost", 27017)
    self.db = conn['markets']
    