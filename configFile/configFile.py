import datetime

from flask import Blueprint, request, g, jsonify, json

config = Blueprint('configFile', __name__)

# 通过username查出个人的所有类别
@config.route('/config',methods=['GET'])
def init() :
    print("Hello Config")

# Test
@config.route('/configtest', methods=['GET'])
def Login():
    select_list = []
    select_result = g.mongo.db.ConfigFile.find({"userid":"1001"})
    for s in select_result:
        select_list.append({"config": s["config"]})
    return jsonify({'code': 200, 'meaasge': 'dsd', 'data': select_list})

# Select Config By Userid
@config.route('/selectConfigByUserid',methods=['GET'])
def selectConfigByUserid():
    selectResult = []
    userid = request.args.get('userid')

    if userid:
        try:
            selectResult = g.mongo.db.ConfigFile.find_one({"userid":userid})
        except Exception:
            return jsonify({'code': 300, 'meaasge': 'Select Fail', 'data': Exception})
        else:
            return jsonify({'code': 200, 'meaasge': 'Select Success', 'data': selectResult['config']})
    else:
        return jsonify({'code': 301, 'meaasge': 'No UserID', 'data': ''})

# Create a configuration file in the configuration table
@config.route('/changeconfig', methods=['POST'])
def changeConfig():
    userid = request.form.get('userid')
    configfile = json.loads(request.form.get('config'))

    select_result = g.mongo.db.ConfigFile.find({"userid": userid})
    print(select_result.count())

    if select_result.count() != 0:
        try:
            g.mongo.db.ConfigFile.update({'userid': userid}, { 'userid':userid,'config': configfile})
        except Exception:
            return jsonify({'code': 300, 'meaasge': 'Update Fail', 'data': Exception})
        else:
            return jsonify({'code': 200, 'meaasge': 'Update Success', 'data': ''})
    else:
        try:
            g.mongo.db.ConfigFile.insert({'userid':userid,'config':configfile})
        except Exception:
            return jsonify({'code': 300, 'meaasge': 'Insert Fail', 'data': ''})
        else:
            return jsonify({'code': 200, 'meaasge': 'Insert Success', 'data': ''})