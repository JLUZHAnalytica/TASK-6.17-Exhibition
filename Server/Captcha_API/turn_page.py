from flask import Flask
from pymongo import MongoClient

#翻页
client = MongoClient()
db = client['test']
def page_query(page=1,limit=20,table='test'):
    collection = db[table]
    return(list(collection.find().skip((page-1)*limit).limit(limit)))
page_query()

web = Flask(__name__)