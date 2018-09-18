import datetime

from flask import Blueprint, request, g, jsonify, json
from pymongo import DESCENDING

log = Blueprint('log', __name__)

# Test
@log.route('/logtest', methods=['GET'])
def Login():
    select_list = []
    select_result = g.mongo.db.tasklog.find({"taskid":"2036f13c-7ad5-11e8-adbe-0016413cb304"})

    for s in select_result:
        select_list.append({"taskName": s["taskName"], "description": s["description"]})
    return jsonify({'code': 200, 'meaasge': 'Login Fail', 'data': select_list})

# Query the last running record for a single task
@log.route('/selectCount',methods = ['GET'])
def selectCount():
    select_list = []
    taskid = request.args.get('taskid');
    if taskid:
        try:
            select_result = g.mongo.db.tasklog.find({'taskid':taskid}).sort('resultTime', DESCENDING)
            if select_result.count() >0:
                select_list = select_result[0]
                select_list.pop("_id")
            else:
                return jsonify({'code': 201, 'meaasge': 'No Result', 'data': ''})

        except Exception as e:
            return jsonify({'code': 300, 'meaasge': 'Select Fail', 'data': str(e)})
        else:
            return jsonify({'code': 200, 'meaasge': 'Select Success', 'data': select_list})
    else:
        return jsonify({'code': 301, 'meaasge': 'No TaskID', 'data': ''})

@log.route('/selectCountList', methods= ['GET'])
def selectCountList():
    select_list = []
    taskid = request.args.get('taskid');
    if taskid:
        try:
            select_result = g.mongo.db.tasklog.find({'taskid': taskid}).sort('resultTime', DESCENDING)
            select_temp = {}
            for s in select_result:
                select_temp[s['resultTime']]=s['log_info']['result']
            select_list.append(select_temp)
        except Exception as e:
            return jsonify({'code': 300, 'meaasge': 'Select Fail', 'data': str(e)})
        else:
            return json.dumps({'code': 200, 'meaasge': 'Select Success', 'data': select_list}, sort_keys=False)
    else:
        return jsonify({'code': 301, 'meaasge': 'No TaskID', 'data': ''})

@log.route('/selectCountTable', methods= ['POST'])
def selectCountTable():
    select_list = []
    taskids = json.loads(request.form.get('taskids'));

    print(type(taskids))
    if taskids:
        try:
            select_result = g.mongo.db.tasklog.find({"taskid":{"$in": taskids}}).sort('resultTime', DESCENDING)
            for s in select_result:
                s.pop("_id")
                select_list.append(s)
        except Exception as e:
            return jsonify({'code': 300, 'message': 'Select Fail', 'data': str(e)})
        else:
            return json.dumps({'code': 200, 'meaasge': 'Select Success', 'data': select_list}, sort_keys=False)
    else:
        return jsonify({'code':301, 'message': 'No TaskIDs', 'data': ''})

@log.route('/selectCountChart', methods= ['GET'])
def selectCountChart():
    select_list = []
    taskid = request.args.get('taskid');
    if taskid:
        try:
            select_result = g.mongo.db.tasklog.find({'taskid': taskid}).sort('resultTime', 1)
            for s in select_result:
                select_list.append({"resultTime": s["resultTime"],"result": s["log_info"]["result"]})
                s.pop("_id")
        except Exception as e:
            return jsonify({'code': 300, 'message': 'Select Fail', 'data': str(e)})
        else:
            return json.dumps({'code': 200, 'message': 'Select Success', 'data': select_list}, sort_keys=False)
    else:
        return jsonify({'code': 301, 'message': 'No TaskIds', 'data': ''})