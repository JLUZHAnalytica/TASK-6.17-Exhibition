from pymongo import MongoClient
from flask import Flask
from flask import request,make_response
from json import dumps
from flask_cors import CORS
import json
from bson import ObjectId

web = Flask(__name__)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
##################################################
@web.after_request
def af_request(resp):
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'Get,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp
##################################################
CORS(web,supports_credentials=True)
client = MongoClient()

def page_query(page=1,limit=20,table='test'):
    collection = client['test']['test']
    return(list(collection.find().skip((page-1)*limit).limit(limit)))

def page_count():
    collection = client['test']['test']
    return collection.find().count()

@web.route('/ai_code')
def img():
    page = int(request.args.get('page','1'))
    limit = int(request.args.get('limit','20'))
    data = page_query(page=page,limit=limit,)
    response_data=(data)
    return dumps(response_data,cls=JSONEncoder)

web.run()