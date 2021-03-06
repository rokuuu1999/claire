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
        res = database.cookies_query(res)

        if res == {}:
            outcome = {"code": 500, "msg": "用户身份不存在"}
        elif res["expireTime"] > now:
            outcome = {"code": 200, "msg": "cookies未过期"}
        elif res["expireTime"] <= now:
            outcome = {"code": 500, "msg": "cookies已过期"}
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
        elif user_repassword != user_password:
            resp = ({"code": 500, "msg": "密码不一致"})
        else:
            resp = ({"code": 500, "msg": "注册失败,请核验信息"})
        return resp


@app.route('/post', methods=['GET'])
def detail_of_page():
    id = request.args.get("id")
    type = request.args.get("type")

    if type == '0':
        article = database.article(id)
        article['nickName'] = database.query_username(article['userId'])
        article['avatarUrl'] = database.query_avatarUrl(article['userId'])
        result = {"code": 200, "msg": "查找文章成功", "contain": article}
    elif type == '1':
        idea = database.idea(id)
        idea['nickName'] = database.query_username(idea['userId'])
        idea['avatarUrl'] = database.query_avatarUrl(idea['userId'])
        result = {"code": 200, "msg": "查找想法成功", "contain": idea}
    elif type == '2':
        video = database.video(id)
        video['nickName'] = database.query_username(video['userId'])
        video['avatarUrl'] = database.query_avatarUrl(video['userId'])
        result = {"code": 200, "msg": "查找视频成功", "contain": video}
    else:
        result = {"code": 500, "msg": "请检查参数是否正确", }
    return make_response(result)


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
        res = database.publish_query_nskips(page * 3)
        homePageList = []
        if not res:
            res = {"code": 500, "msg": "没有数据可以返回"}
            return make_response(res)

        for publish in res:
            if publish["type"] == 0:
                result = database.article(publish["parentId"])
            elif publish["type"] == 1:
                result = database.idea(publish["parentId"])
            else:
                result = database.video(publish["parentId"])
            result["type"] = publish["type"]
            result["authorName"] = database.query_username(result['userId'])
            result["avatarUrl"] = database.query_avatarUrl(result['userId'])
            result['publishId'] = result.pop("_id")
            del result['userId']
            homePageList.append(result)

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
        commentNum = 0
        likeNum = 0
        comments = []
        hot = 0
        if not (userId and createTime and title and subTitle and articleContent and
                classify and tags and cover):
            return make_response({"code": 500, "msg": "所有元素必须填写"})
        else:
            _id = database.article_insert(createTime, userId, title, subTitle, commentNum, likeNum, comments,
                                          articleContent, classify, tags, cover, hot)
            database.publish_insert(_id, createTime, 0)
            database.insert_tag(tags)
            resp = {"code": 200, "msg": "插入文章成功"}
            return make_response(resp)


@app.route('/publishIdea', methods=['POST'])
def thinking():
    if request.method == 'POST':
        userId = request.cookies.get('userId')
        createTime = request.form.get("createTime")
        pics = json.loads(request.form.get("pics"))
        ideaContent = request.form.get("content")
        classify = request.form.get("classify")
        tags = json.loads(request.form.get("tags"))
        commentNum = 0
        likeNum = 0
        comments = []
        if not (userId and createTime and pics and ideaContent and
                classify and tags):
            return make_response({"code": 500, "msg": "所有元素必须填写"})
        else:
            _id = database.thinking_insert(createTime, userId, commentNum, likeNum, comments,
                                           ideaContent, classify, tags, pics)
            database.publish_insert(_id, createTime, 1)
            database.insert_tag(tags)
            return make_response({"code": 200, "msg": "插入想法成功"})


@app.route('/publishVideo', methods=['POST'])
def movie_camera():
    if request.method == 'POST':
        userId = request.cookies.get('userId')
        createTime = request.form.get("createTime")
        videoUrl = request.form.get("videoUrl")
        title = request.form.get("title")
        classify = request.form.get("classify")
        tags = json.loads(request.form.get("tags"))
        commentNum = 0
        likeNum = 0
        comments = []
        if not (userId and createTime and videoUrl and
                classify and tags):
            return make_response({"code": 500, "msg": "所有元素必须填写"})
        else:
            _id = database.video_insert(createTime, userId, title, commentNum, likeNum, comments,
                                        classify, tags, videoUrl)
            database.publish_insert(_id, createTime, 2)
            database.insert_tag(tags)
            return make_response({"code": 200, "msg": "插入video成功"})


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


@app.route('/comment', methods=['GET'])
def commentquery():
    if request.method == 'GET':
        pageId = request.args.get('parentId')
        comment = database.comment(pageId)
        pageList = {}
        type = request.args.get('type')
        if type == '0':
            article = database.article(pageId)
            pageList = article
        elif type == '1':
            idea = database.idea(pageId)
            pageList = idea
        elif type == '2':
            video = database.video(pageId)
            pageList = video
        pageList['comment'] = []  # [comment]
        pageList['likeNum'] = 0
        pageList['commentNum'] = 0
        pageList["authorName"] = database.query_username(pageList["userId"])
        pageList["avatarUrl"] = database.query_avatarUrl(pageList["userId"])
        del pageList['userId']
        return make_response({"code": 200, "msg": "查询成功", "page": pageList})


@app.route('/popularArticle', methods=['GET'])
def firearticle():
    if request.method == 'GET':
        top5_article = database.fire_article()
        articleList = []
        if top5_article:
            for article in top5_article:
                articleList.append(article)
            return make_response({"code": 200, "msg": "查取五篇热门成功", "articleList": articleList})
        else:
            return False


@app.route('/tagQuery/<tagName>', methods=['GET'])
def tag_query_article(tagName):
    if request.method == 'GET':
        contain = database.tag_query(tagName)
        return make_response({"code": 200, "msg": "根据标签查询成功", "publishList": contain})
    else:
        return False
