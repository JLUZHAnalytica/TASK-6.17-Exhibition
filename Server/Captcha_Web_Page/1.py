from flask import Flask
from flask import request
from pymongo import MongoClient
from json import dumps

'''内容不用学部分(运行不了)
import json
from bson import OBJectId
class JSONEncoder(json.JSONEncoder):
    def default(self,o):
        if isinstance(o,ObjectId):
            return str(o)
        return json.JSONEncoder.default(self,o)
'''
web = Flask(__name__)
client = MongoClient()
img_collection=client["img_url"]["test"]
def fanye(page=1,limit_n=2):
    pages=(page-1)*limit_n
    return list(img_collection.find().skip(pages).limit(limit_n))#这里显示语法错误，但是可以运行
@web.route("/Server/Captcha_Web_Page/1")
def shuchu():
    page = int(request.args.get("page","1"))
    limit = int(request.args.get("limit","20"))
    return str(fanye(page=1))
web.run()
