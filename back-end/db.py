import pymongo
from uuid import uuid4
from setting import *


# Python 面向对象写法
class db:
    def __init__(self):
        self.myClient = self.myDB = None
        self.connect()
        self.userCL = self.myDB["UserInfo"]
        self.cookieCL = self.myDB["Cookies"]
        self.articleCL = self.myDB["Articles"]

    def connect(self):
        self.myClient = pymongo.MongoClient(
            "mongodb://{user}:{password}@{ip}:27017/{db}".format(user=USER, password=PASSWORD, ip=IP, db=AUTH_DB))
        self.myDB = self.myClient["clay"]

    def login(self, userName):
        return self.userDB.find_one({"userName": userName})

    def register(self, user_id, user_name, user_email, user_password):
        mydict = {"userId": user_id, "userName": user_name, "email": user_email, "password": user_password,
                  "avatarUrl": "https://pic2.zhimg.com/da8e974dc_xll.jpg", "userAuthority": 1, "like": [],
                  "comments": [],
                  "publish": []}
        self.userCL.insert_one(mydict)

    def cookies(self, userid, time):
        self.cookieCL.update({"userId": userid}, {"userId": userid, "expireTime": time}, True)

    def cookies_query(self, userid):
        return self.cookieCL.find_one({"userId": userid})

    def cookies_query_expireTime(self, expireTime):
        return self.cookieCL.find_one({"expireTime": expireTime})

    def article(self, aid):
        mycol = self.mydb["Articles"]
        myquery = {"selfId": aid}
        mydoc = mycol.find(myquery)
        res = mydoc
        return res

    def tags(self, tid):
        mycol = self.mydb["Tags"]
        myquery = {"selfId": tid}
        mydoc = mycol.find(myquery)
        res = mydoc
        return res

    def articleimg(self, iid):
        mycol = self.mydb["Imgs"]
        myquery = {"selfId": iid}
        mydoc = mycol.find(myquery)
        res = mydoc
        return res

    def publish_query_nskips(self, num):
        mycol = self.mydb["Publish"]
        res = mycol.find().sort("createTime", -1).skip(num).limit(5)
        publishList = []
        for item in res:
            publishList.append(item)
        return publishList

    def query_username(self, userid):
        mycol = self.mydb["UserInfo"]
        myquery = {"userId": userid}
        mydoc = mycol.find(myquery, {"userName": 1})
        if mydoc != None:
            username = mydoc["userName"]
            return username
        else:
            return ""
        return username

    def query_avatarUrl(self, userid):
        mycol = self.mydb["UserInfo"]
        myquery = {"userId": userid}
        mydoc = mycol.find(myquery, {"avatarUrl": 1})
        avatarUrl = mydoc["avatarUrl"]
        return avatarUrl

    def query_tagList(self):
        mycol = self.mydb["Tags"]
        tagList = mycol.find().pretty()
        return tagList

    def thinking_insert(self, createTime, userId, ideaContent, classify, tags,
                        pics, authorName, avatarURL):
        mycol = self.mydb["Ideas"]
        mycol.insert({"createTime": createTime, "userId": userId, "ideaContent": ideaContent
                         , "classify": classify, "tags": tags, "pics": pics, "authorName": authorName,
                      "avatarURL": avatarURL})
        id = mycol.find({"createTime": createTime})
        return id

    def publish_insert(self, parentId, createTime, type):
        mycol = self.mydb["Publish"]
        mycol.insert({"parentId": parentId, "createTime": createTime, "type": type})
        id = mycol.find({"createTime": createTime})
        return id

    def video_insert(self, title, videoUrl, userId, authorName, avatarURL, createTime, classify, tags, cover):
        mycol = self.mydb["Videos"]
        mycol.insert(
            {"createTime": createTime, "userId": userId, "authorName": authorName, "videoUrl": videoUrl, "title": title,
             "classify": classify, "tags": tags, "cover": cover})
        id = mycol.find({"createTime": createTime})
        return id

    def article_insert(self, createTime, userId, title, subTitle, articleContent, classify, tags
                       , cover, pics):
        _id = uuid4()
        self.articleCL.insert({"_id": _id,
                               "userId": userId,
                               "Title": title,
                               "subTitle": subTitle,
                               "createTime": createTime,
                               "articleContent": articleContent,
                               "classify": classify,
                               "tags": tags,
                               "cover": cover,
                               "pics": pics,
                               })
        return _id
