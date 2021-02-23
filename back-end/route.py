import json
from app import app, database
from flask import request, make_response
from function import *
from datetime import datetime
from setting import *
from flask import request
import time


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        res = request.cookies.get('userId')
        now = time.time()
        expireTime = database.cookies_query(res)["expireTime"]
        if expireTime > now:
            outcome = {"code": 200, "msg": "cookies未过期"}
            resp = make_response(outcome)
            return resp
        elif expireTime <= now:
            outcome = {"code": 500, "msg": "cookies已过期"}
            resp = make_response(outcome)
            return resp
        else:
            outcome = {"code": 500, "msg": "未查询到cookies，请重新登录"}
            resp = make_response(outcome)
            return resp

    elif request.method == 'POST':
        # 不用明白为什么，暂时这么用

        res = json.loads(request.get_data(as_text=True))

        user_name = res['username']
        user_email = res['email']
        user_password = res['password']
        data = database.login(user_name)
        if data["password"] == user_password:
            outcome = {"userId": data["userId"], "authroity": data["userAuthority"], "avatarUrl": data["avatarUrl"]}
            resp = make_response(outcome)
            timeout = time.time() + 60 * 60 * 24
            resp.set_cookie('userId', data["userId"], expires=timeout)  # , domain="localhost")
            database.cookies(data["userId"], timeout)
            return resp
        else:
            outcome = {"code": 500, "msg": "登录失败"}
            resp = make_response(outcome)
            return resp


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 不用明白为什么
        res = json.loads(request.get_data(as_text=True))
        print(res)
        user_name = res['userName']
        user_email = res['email']
        user_password = res['password']
        user_repassword = res['repassword']
        user_id = md5(user_name + PRIVATE_KEY)
        if database.queryusername(user_id) == user_name:
            outcome = {"code": 500, "msg": "用户名重复"}
            resp = make_response(outcome)
            return resp
        elif user_repassword == user_password:
            database.register(user_id, user_name, user_email, user_password)
            outcome = {"code": 200, "msg": "注册成功"}
            resp = make_response(outcome)
            return resp
        else:
            outcome = {"code": 200, "msg": "注册失败"}
            resp = make_response(outcome)
            return resp


@app.route('/article', methods=['GET', 'POST'])
def articles():
    if request.method == 'GET':
        res = json.loads(request.get_data(as_text=True))
        aid = res['aid']
        result = database.article(aid)
        outcome = {"aid": result[0], "articleTile": result[1], "subTitle": result[2],
                   "articleContent": result[3], "userId": result[4], "createtime": result[5],
                   "commentNum": result[6], "likeNum": result[7], "classify": result[8]}
        resp = make_response(outcome)
        return resp
    else:
        return "fail"


@app.route('/tags', methods=['GET', 'POST'])
def tags():
    if request.method == 'GET':
        res = json.loads(request.get_data(as_text=True))
        tid = res['tid']
        result = database.tags(tid)
        outcome = {"tid": result[0], "tagname": result[1]}
        resp = make_response(outcome)
        return resp
    else:
        return "fail"


@app.route('/articleImg', methods=['GET', 'POST'])
def articleImg():
    if request.method == 'GET':
        res = json.loads(request.args.get("IId"))
        iid = res['IID']
        result = database.articleimg(iid)
        outcome = {"IID": result[0], "imgurl": result[1]}
        resp = make_response(outcome)
        return resp
    else:
        return "fail"


@app.route('/homepage', methods=['GET'])
def homepage():
    if request.method == 'GET':
        page = json.loads(request.args.get("page"))
        publishList = database.publish_query_nskips(page * 5)
        return make_response("publishList")


@app.route('/uploadFile', methods=['POST'])
def upload():
    if request.method == 'POST':
        print(request.files.get("pic"))
        return "ss"
