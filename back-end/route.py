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
        elif expireTime <= now:
            outcome = {"code": 500, "msg": "cookies已过期"}
            resp = make_response(outcome)
        else:
            outcome = {"code": 500, "msg": "未查询到cookies，请重新登录"}
            resp = make_response(outcome)
    else:
        res = json.loads(request.get_data(as_text=True))

        user_name = res['username']
        user_password = res['password']

        data = database.login(user_name)

        if data["password"] == user_password:
            timeout = time.time() + 60 * 60 * 24
            database.cookies(data["userId"], timeout)

            outcome = {"userId": data["userId"], "authroity": data["userAuthority"], "avatarUrl": data["avatarUrl"]}
            resp = make_response(outcome)
            resp.set_cookie('userId', data["userId"], expires=timeout)
        else:
            outcome = {"code": 500, "msg": "登录失败"}
            resp = make_response(outcome)
    return resp


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        res = json.loads(request.get_data(as_text=True))
        user_name = res['userName']
        user_email = res['email']
        user_password = res['password']
        user_repassword = res['repassword']

        user_id = md5(user_name + PRIVATE_KEY)

        if database.query_username(user_id):
            resp = make_response({"code": 500, "msg": "用户名重复"})
        elif user_repassword == user_password:
            database.register(user_id, user_name, user_email, user_password)
            resp = make_response({"code": 200, "msg": "注册成功"})
        else:
            resp = ({"code": 500, "msg": "注册失败"})
        return resp


@app.route('/article', methods=['GET'])
def articles():
    aid = request.args.get('aid')
    article = database.article(aid)

    # 有问题
    outcome = {"aid": article[0], "articleTile": article[1], "subTitle": article[2],
               "articleContent": article[3], "userId": article[4], "createTime": article[5],
               "commentNum": article[6], "likeNum": article[7], "classify": article[8]}
    result = {"code": 200, "msg": "请求成功", "contain": outcome}
    resp = make_response(result)
    return resp


@app.route('/tags', methods=['GET'])
def tags():
    if request.method == 'GET':
        res = json.loads(request.get_data(as_text=True))
        tid = res['tid']
        result = database.tags(tid)

        # 有问题
        outcome = {"tid": result[0], "tagname": result[1]}

        return make_response({"code": 200, "msg": "请求成功", "contain": outcome})


@app.route('/homepage', methods=['GET'])
def homepage():
    if request.method == 'GET':
        page = request.args.get("page")
        publishList = database.publish_query_nskips(page * 5)
        for publish in publishList:
            if publish.type == 0:
                database.article(publish._id)
        result = {"code": 200, "msg": "请求成功", "publishList": publishList}
        resp = make_response(result)
        return resp
    else:
        outcome = {"code": 500, "msg": "请求失败"}
        resp = make_response(outcome)
        return resp


@app.route('/publishArticle', methods=['POST'])
def blue_book():
    if request.method == 'POST':
        userId = request.cookies.get('userId')
        authorName = database.query_username(userId)
        avatarURL = database.query_avatarUrl(userId)

        createTime = request.form.get("createTime")
        pics = request.form.get("pics")
        title = request.form.get("title")
        subTitle = request.form.get("subTitle")
        articleContent = request.form.get("articleContent")
        classify = request.form.get("classify")
        tags = request.form.get("tags")
        cover = request.form.get("cover")

        _id = database.article_insert(createTime, userId, title, subTitle,
                                      articleContent, classify, tags, cover,
                                      pics, authorName, avatarURL)
        database.publish_insert(_id, createTime, 0)
        resp = {"code": 200, "msg": "插入文章成功"}
    else:
        outcome = {"code": 500, "msg": "写入文章失败"}
        resp = make_response(outcome)
    return resp


@app.route('/publishIdea', methods=['POST'])
def thinking():
    if request.method == 'POST':
        res = request.cookies.get('expireTime')
        userId = str(database.cookies_query_expiretime(res))
        createTime = request.form.get("createTime")
        authorName = request.form.get("authorName")
        avatarURL = request.form.get("avatarURL")
        pics = request.form.get("pics")
        ideaContent = request.form.get("ideaContent")
        classify = request.form.get("classify")
        tags = request.form.get("tags")
        document = database.thinking_insert(createTime, userId,
                                            ideaContent, classify, tags,
                                            authorName, avatarURL, pics)
        id = document[0]
        database.publish_insert(id, createTime, 1)
        result = {"code": 200, "msg": "插入想法成功"}
        return make_response(result)
    else:
        outcome = {"code": 500, "msg": "想法插入失败"}
        resp = make_response(outcome)
        return resp


@app.route('/publishVideo', methods=['POST'])
def movie_camera():
    if request.method == 'POST':
        res = request.cookies.get('expireTime')
        userId = str(database.cookies_query_expiretime(res))
        createTime = request.form.get("createTime")
        authorName = database.query_username(userId)
        videoUrl = request.form.get("videoUrl")
        title = request.form.get("title")
        classify = request.form.get("classify")
        tags = request.form.get("tags")
        avatarURL = database.query_avatarUrl(userId)
        cover = request.form.get("cover")
        document = database.video_insert(createTime, userId, title,
                                         classify, tags, cover,
                                         authorName, videoUrl, avatarURL)
        id = document[0]
        database.publish_insert(id, createTime, 2)
        result = {"code": 200, "msg": "插入video成功"}
        resp = make_response(result)
    else:
        outcome = {"code": 500, "msg": "写入video失败"}
        resp = make_response(outcome)
    return resp


@app.route('/uploadFile', methods=['POST'])
def upload():
    if request.method == 'POST':
        myKodo = kodo()
        file = request.files.get("file")
        fileType = request.form.get("type")
        fileName = "{name}.{type}".format(name=str(uuid.uuid4()), type=fileType)
        filePath = "./tmp/" + fileName
        file.save(filePath)
        fileURL = "http://kodo.wendau.com/" + myKodo.upload(fileName)
        os.remove(filePath)
        resp = make_response({"code": 200, "msg": "上传文件成功", "fileURL": fileURL})
    else:
        resp = make_response({"code": 500, "msg": "上传文件失败"})
    return resp
