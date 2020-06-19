# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
'''将数据导入数据库'''
import json
from pymongo import MongoClient

client = MongoClient()
with open('newcompany_info_list.json','r',encoding='utf-8')as f:
    company_info_list = json.loads(f.read())
company_info_list_collection = client['test-database']['company_list']
company_info_list_collection.insert_many(company_info_list)
print('数据导入成功!')