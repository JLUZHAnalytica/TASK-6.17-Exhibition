import json
from pymongo import MongoClient

client = MongoClient()
with open('Data/newcaptcha_img_list.json','r',encoding='utf-8')as f:
    img_url = json.loads(f.read())
img_url_collection = client['test']['test']
img_url_collection.insert_many(img_url)
print('数据导入成功!')