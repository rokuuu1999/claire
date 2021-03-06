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
        user_name = request.form.get("username")
        user_password = request.form.get("password")

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
        user_name = request.form.get('userName')
        user_email = request.form.get('email')
        user_password = request.form.get('password')
        user_repassword = request.form.get('repassword')
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
    del article['userId']
    # 有问题
    outcome = article
    result = {"code": 200, "msg": "请求成功", "contain": outcome}
    resp = make_response(result)
    return resp


@app.route('/tags', methods=['GET'])
def tags():
    if request.method == 'GET':
        tagList = []
        for tag in database.hot_tags():
            tagList.append(tag["tagName"])
        return make_response({"code": 200, "msg": "请求成功", "tagList": tagList})


@app.route('/homepage', methods=['GET'])
def homepage():
    if request.method == 'GET':
        page = int(request.args.get("page"))
        res = database.publish_query_nskips(page * 5)
        homePageList = {}
        if res == "null":
            res = {"code":500,"msg":"没有数据可以返回"}
            return make_response(res)
        for publish in res:

            if publish["type"] == 0:
                result = database.article(publish["parentId"])

                result["userName"] = database.query_username(result['userId'])
                result["avatarUrl"] = database.query_avatarUrl(result['userId'])
                del result['_id']
                del result['userId']

                result.append(homePageList)

            elif publish["type"] == 1:
                result = database.idea(publish["parentId"])

                result["userName"] = database.query_username(result['userId'])
                result["avatarUrl"] = database.query_avatarUrl(result['userId'])
                del result['_id']
                del result['userId']
                result.append(homePageList)

            elif publish["type"] == 2:
                result = database.video(publish["parentId"])
                result["userName"] = database.query_username(result['userId'])
                result["avatarUrl"] = database.query_avatarUrl(result['userId'])
                del result['_id']
                del result['userId']
                result.append(homePageList)

        res = {"code": 200, "msg": "请求成功", "publishList": homePageList}
        return make_response(res)


@app.route('/publishArticle', methods=['POST'])
def blue_book():
    if request.method == 'POST':
        userId = request.cookies.get('userId')

        createTime = request.form.get("createTime")
        title = request.form.get("title")
        subTitle = request.form.get("subTitle")
        articleContent = request.form.get("articleContent")
        classify = request.form.get("classify")
        tags = json.loads(request.form.get("tags"))
        cover = request.form.get("cover")

        _id = database.article_insert(createTime, userId, title, subTitle,
                                      articleContent, classify, tags, cover,
                                      )
        database.publish_insert(_id, createTime, 0)
        resp = {"code": 200, "msg": "插入文章成功"}
    else:
        outcome = {"code": 500, "msg": "写入文章失败"}
        resp = make_response(outcome)
    return resp


@app.route('/publishIdea', methods=['POST'])
def thinking():
    if request.method == 'POST':
        userId = request.cookies.get('userId')

        createTime = request.form.get("createTime")

        pics = json.loads(request.form.get("pics"))
        ideaContent = request.form.get("content")

        classify = request.form.get("classify")
        tags = json.loads(request.form.get("tags"))
        _id = database.thinking_insert(createTime, userId,
                                       ideaContent, classify, tags, pics)

        database.publish_insert(_id, createTime, 1)
        database.insert_tag(tags)
        resp = make_response({"code": 200, "msg": "插入想法成功"})

    else:
        outcome = {"code": 500, "msg": "想法插入失败"}
        resp = make_response(outcome)
    return resp


@app.route('/publishVideo', methods=['POST'])
def movie_camera():
    if request.method == 'POST':
        userId = request.cookies.get('userId')
        createTime = request.form.get("createTime")
        videoUrl = request.form.get("videoUrl")
        title = request.form.get("title")
        classify = request.form.get("classify")
        tags = json.loads(request.form.get("tags"))
        _id = database.video_insert(createTime, userId, title,
                                    classify, tags, videoUrl)

        database.publish_insert(_id, createTime, 2)
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

# def comment():
#    if request.method == 'GET':
#        userId = request.
