# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:05:29 2020

将前程无忧的公司工作岗位插入到数据库

@author: Spirit H
"""


from pymongo import MongoClient
import json
from time import sleep

def new_framework(num , job_list):
    try:
        return job_list[num]
    except Exception:
        return ''
        

client = MongoClient("mongodb://localhost:27017/") # 实例化数据库对象
db = client["job51"] # 新建一个数据库job
db_sheet = db["job_list"] # 新建一个数据表job_list
#db_sheet.insert_one({'nothing':'nothing'})
#db_sheet.drop()
print(client.list_database_names())
print(db.list_collection_names())
sleep(5)

# 读取岗位信息

with open('Data/jobs_list.json' , 'r' , encoding = 'utf-8') as f: 
    print('reading json')
    job = f.read()
    job = json.loads(job)
print('get json data')
    
# 获得所有公司名称 共229015个

company_list = []
for key in job:
    company_list.append(key)
    #break
print('get company_list')

# 构建数据结构

data_list = [] # 记录结构化的数据
t = 0 # 记录公司数量
for name in company_list:
    job_list = job[name] # 单个公司的所有职位列表
    for i in range(len(job_list)): # 遍历每个职位
        Name = ''
        Experience = ''
        Degree = ''
        Need = ''
        Area = ''
        Salary = ''
        URL = ''
        for j in range(len(job_list[i])): # 遍历职位的每个元素
            if j == 0:
                Name = new_framework(j, job_list[i])
            if j == 1:
                Experience = new_framework(j, job_list[i])
            if j == 2:
                Degree = new_framework(j, job_list[i])
            if j == 3:
                Need = new_framework(j, job_list[i])
            if j == 4:
                Area = new_framework(j, job_list[i])
            if j == 5:
                Salary = new_framework(j, job_list[i])
            if j == 6:
                URL = new_framework(j, job_list[i])
        data_list.append({'id':i , 'company':name , 'Name':Name , 'Experience':Experience , 'Degree':Degree , 'Need':Need ,
                      'Area':Area , 'Salary':Salary , 'URL':URL})
    t = t+1
    print('{}/229015'.format(t))
print('get data_list')

print('start inserting')
db_sheet.insert_many(data_list)
print('done')
print('checking data')
print(client.list_database_names())
print(db.list_collection_names())
print(db_sheet.find().count()) # 共 3283171 个岗位