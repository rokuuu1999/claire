import pymongo
from uuid import uuid4
from setting import *


class db:
    def __init__(self):
        self.myClient = self.myDB = {}
        self.connect()
        self.userCL = self.myDB["UserInfo"]
        self.cookieCL = self.myDB["Cookies"]
        self.articleCL = self.myDB["Articles"]
        self.videosCL = self.myDB["Videos"]
        self.publishCL = self.myDB["Publish"]
        self.ideasCL = self.myDB["Ideas"]
        self.tagCl = self.myDB["tag"]
        self.commentCL = self.myDB["Comments"]

    def connect(self):
        self.myClient = pymongo.MongoClient(
            "mongodb://{user}:{password}@{ip}:27017/{db}".format(user=USER, password=PASSWORD, ip=IP, db=AUTH_DB))
        self.myDB = self.myClient["clay"]

    def login(self, userName):
        res = self.userCL.find_one({"userName": userName})
        if res:
            return res
        else:
            return False

    def register(self, user_id, user_name, user_email, user_password):
        mydict = {"userId": user_id, "userName": user_name, "email": user_email, "password": user_password,
                  "avatarUrl": "https://pic2.zhimg.com/da8e974dc_xll.jpg", "userAuthority": 1, "like": [],
                  "comments": [],
                  "publish": []}
        self.userCL.insert_one(mydict)

    # UserInfo
    def query_username(self, userId):
        res = self.userCL.find_one({"userId": userId})["userName"]
        if res:
            return res
        else:
            return False

    def query_avatarUrl(self, userId):
        res = self.userCL.find_one({"userId": userId})["avatarUrl"]
        if res:
            return res
        else:
            return False

    # Cookie
    def cookies(self, userid, time):
        res = self.cookieCL.update({"userId": userid}, {"userId": userid, "expireTime": time}, True)
        if res:
            return True
        else:
            return False

    def cookies_query(self, userid):
        res = self.cookieCL.find_one({"userId": userid})
        if res:
            return res
        else:
            return {}

    # Article

    def article(self, aid):
        res = self.articleCL.find_one({"_id": aid})
        if res:
            return res
        else:
            return False

    def hot_articles(self):
        pass

    def article_insert(self, createTime, userId, title, subTitle,
                       articleContent, classify, tags, cover,
                       ):
        _id = str(uuid4())
        self.articleCL.insert({"_id": _id,
                               "userId": userId,
                               "Title": title,
                               "subTitle": subTitle,
                               "createTime": createTime,
                               "articleContent": articleContent,
                               "classify": classify,
                               "tags": tags,
                               "cover": cover,

                               })
        return _id

    # Tag
    def insert_tag(self, tags):
        for tag in tags:
            self.tagCl.update({"tagName": tag}, {
                "$inc": {"num": 1},
            }, upsert=True)

    def hot_tags(self):
        res = self.tagCl.find().sort("num", -1).limit(10)
        if res:
            return res
        else:
            return False

    # Idea
    def idea(self, iid):
        res = self.ideasCL.find_one({"_id": iid})
        if res:
            return res
        else:
            return False

    def thinking_insert(self, createTime, userId,
                        ideaContent, classify, tags, pics):
        _id = str(uuid4())
        self.ideasCL.insert({
            "_id": _id,
            "createTime": createTime,
            "userId": userId,
            "ideaContent": ideaContent,
            "classify": classify,
            "tags": tags,
            "pics": pics,
        })
        return _id

    # Video
    def video(self, vid):
        res = self.videosCL.find_one({"_id": vid})
        if res:
            return res
        else:
            return False

    def video_insert(self, createTime, userId, title,
                     classify, tags, videoUrl):
        _id = str(uuid4())
        self.videosCL.insert({
            "_id": _id,
            "title": title,
            "videoUrl": videoUrl,
            "userId": userId,

            "createTime": createTime,
            "classify": classify,
            "tags": tags,

        })
        return _id

    # Publish
    def publish_insert(self, parentId, createTime, type):
        self.publishCL.insert({
            "parentId": parentId,
            "createTime": createTime,
            "type": type,
        })

    def publish_query_nskips(self, num):
        mycol = self.myDB["Publish"]
        res = mycol.find().sort("createTime", -1).skip(num).limit(5)
        publishList = []
        for item in res:
            publishList.append(item)
        return publishList

    # Comment
    def comment(self, id):
        res = self.commentCL.find_one({"_id": id})
        if res:
            return res
        else:
            return False
