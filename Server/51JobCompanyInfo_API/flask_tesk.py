# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
from flask import Flask
from flask import request,make_response
from json import dumps
##数据库
from pymongo import MongoClient
web = Flask(__name__)

##################copy####################json字符串处理-主要是处理  mongodb中的ObjectId
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
###################服务器设置客户端可以跨域访问###################################
from flask_cors import CORS
@web.after_request
def af_request(resp):
    resp = make_response(resp)  ##需要导入一些函数
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp
######################################################

CORS(web, supports_credentials=True)

client = MongoClient()
db = client['test-database']
def page_query(page=1,limit=20,table='company_list'):
    '''翻页查询数据的功能'''
    collection = db[table]
    return list(collection.find().skip((page-1)*limit).limit(limit))

def page_count(table):
    '''总页数'''
    collection = db[table]
    return collection.find().count()

@web.route('/company_list')  ### 接受路由地址数据，还需要接受参数数据/表单数据
def doutu_img():
    page = int(request.args.get('page','1'))
    limit = int(request.args.get('limit','20'))
    table = 'company_list'
    data = page_query(page=page,limit=limit,table=table)
    response_data={"code": 0, "msg": "", "count": page_count(table), "data": data}
    return dumps(response_data,cls=JSONEncoder)

web.run()