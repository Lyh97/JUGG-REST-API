from flask import Flask, session, request, g, jsonify

from bson import ObjectId
from Config import Config
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_restful import Api
from flask_restful import reqparse

from configFile.configFile import config
from log.log import log

parser = reqparse.RequestParser()
# Init flask obj
app = Flask(__name__, static_url_path='')

# Add the CORS-Head to all response of request
CORS(app)

app.config['MONGO_URI'] = 'mongodb://9.42.89.202:27017/log'
api = Api(app)
mongo = PyMongo(app)

def interval_job():
    print('date job')

@app.before_request
def db_connect():
    g.mongo = mongo

app.register_blueprint(config, url_prefix='/configFile')

app.register_blueprint(log, url_prefix='/log')

app.config.from_object(Config())

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True, threaded=True)
