import json
from app import app, database
from flask import make_response
from function import *
from setting import *
from flask import request
import time
import os
import uuid


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
        if database.query_username(user_id) == user_name:
            outcome = {"code": 500, "msg": "用户名重复"}
            resp = make_response(outcome)
            return resp
        elif user_repassword == user_password:
            database.register(user_id, user_name, user_email, user_password)
            outcome = {"code": 200, "msg": "注册成功"}
            resp = make_response(outcome)
            return resp
        else:
            outcome = {"code": 500, "msg": "注册失败"}
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
        result = {"code": 200, "msg": "请求成功", "contain": outcome}
        resp = make_response(result)
        return resp


    else:
        outcome = {"code": 500, "msg": "请求失败"}
        resp = make_response(outcome)
        return resp


@app.route('/tags', methods=['GET', 'POST'])
def tags():
    if request.method == 'GET':
        res = json.loads(request.get_data(as_text=True))
        tid = res['tid']
        result = database.tags(tid)
        outcome = {"tid": result[0], "tagname": result[1]}
        result = {"code": 200, "msg": "请求成功", "contain": outcome}
        resp = make_response(result)
        return resp
    else:
        outcome = {"code": 500, "msg": "请求失败"}
        resp = make_response(outcome)
        return resp


@app.route('/articleImg', methods=['GET', 'POST'])
def articleImg():
    if request.method == 'GET':
        res = json.loads(request.args.get("IId"))
        iid = res['IID']
        result = database.articleimg(iid)
        outcome = {"IID": result[0], "imgurl": result[1]}
        result = {"code": 200, "msg": "请求成功", "contain": outcome}
        resp = make_response(result)
        return resp
    else:
        outcome = {"code": 500, "msg": "请求失败"}
        resp = make_response(outcome)
        return resp


@app.route('/homepage', methods=['GET'])
def homepage():
    if request.method == 'GET':
        page = json.loads(request.args.get("page"))
        publishList = database.publish_query_nskips(page * 5)
        tagList = database.query_tagList()
        result = {"code": 200, "msg": "请求成功", "publishList": publishList, "tagList": tagList}
        resp = make_response(result)
        return resp
    else:
        outcome = {"code": 500, "msg": "请求失败"}
        resp = make_response(outcome)
        return resp


@app.route('/publishIdea', methods=['POST'])
def thinking():
    if request.method == 'POST':
        res = request.cookies.get('expireTime')
        userId =str( database.cookies_query_expiretime(res) )
        createTime = request.form.get("createTime")
        ideaContent = request.form.get("ideaContent")
        classify = request.form.get("classify")
        tags = request.form.get("tags")
        imgs = request.form.get("imgs")
        document = database.thinking_insert(createTime, userId,
                                            ideaContent, classify, tags, imgs)
        type = 1
        id = document[0]
        database.publish_insert(id, createTime, type)
        result = {"code": 200, "msg": "插入成功"}
        return make_response(result)
    else:
        outcome = {"code": 500, "msg": "想法插入失败"}
        resp = make_response(outcome)
        return resp


@app.route('/publishArticle', methods=['POST'])
def blue_book():
    if request.method == 'POST':
        res = request.cookies.get('expireTime')
        userId =str( database.cookies_query_expiretime(res) )
        createTime = request.form.get("createTime")

        title = request.form.get("title")
        subTitle = request.form.get("subTitle")
        articleContent = request.form.get("articleContent")
        classify = request.form.get("classify")
        tags = request.form.get("tags")
        cover = request.form.get("cover")
        document = database.article_insert(createTime, userId, title, subTitle,
                                           articleContent, classify, tags, cover)
        type = 0
        id = document[0]
        database.publish_insert(id, createTime, type)
        result = {"code": 200, "msg": "插入成功"}
        return make_response(result)
    else:
        outcome = {"code": 500, "msg": "写入文章失败"}
        resp = make_response(outcome)
        return resp


@app.route('/uploadFile', methods=['POST'])
def upload():
    if request.method == 'POST':
        kodo = qiniu()
        file = request.files.get("file")
        fileType = request.form.get("type")
        fileName = "{name}.{type}".format(name=str(uuid.uuid4()), type=fileType)
        filePath = "./tmp/" + fileName
        file.save(filePath)
        fileURL = "http://kodo.wendau.com/" + kodo.upload(fileName)
        os.remove(filePath)
        result = {"code": 200, "msg": "上传成功", "fileURL": fileURL}
        resp = make_response(result)
        return resp
    else:
        outcome = {"code": 500, "msg": "上传失败"}
        resp = make_response(outcome)
        return resp
