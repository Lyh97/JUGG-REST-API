import datetime

from flask import Blueprint, request, g, jsonify

log = Blueprint('log', __name__)

# 通过username查出个人的所有类别
@log.route('/log',methods=['GET'])
def init() :
    print("Hello LOG")

# Test
@log.route('/logtest', methods=['GET'])
def Login():
    select_list = []
    select_result = g.mongo.db.tasklog.find({"taskid":"2036f13c-7ad5-11e8-adbe-0016413cb304"})

    for s in select_result:
        select_list.append({"taskName": s["taskName"], "description": s["description"]})
    return jsonify({'code': 200, 'meaasge': 'Login Fail', 'data': select_list})