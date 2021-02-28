import pymongo
from setting import *


# Python 面向对象写法
class db:
    def __init__(self):
        self.connect()

    def connect(self):
        self.myclient = pymongo.MongoClient(
            "mongodb://{user}:{password}@{ip}:27017/{db}".format(user=USER, password=PASSWORD, ip=IP, db=AUTH_DB))
        self.mydb = self.myclient["clay"]

    def login(self, userName):
        mycol = self.mydb["User"]
        myquery = {"userName": userName}
        mydoc = mycol.find_one(myquery)
        res = mydoc
        return res

    def register(self, user_id, user_name, user_email, user_password):
        mycol = self.mydb["User"]
        mydict = {"userId": user_id, "userName": user_name, "email": user_email, "password": user_password,
                  "avatarUrl": "https://pic2.zhimg.com/da8e974dc_xll.jpg", "userAuthority": 1, "like": [],
                  "comments": [],
                  "publish": []}
        mycol.insert_one(mydict)

    def cookies(self, userid, time):
        mycol = self.mydb["Cookies"]
        newCookie = {"userId": userid, "expireTime": time}
        mycol.update({"userId": userid}, newCookie, True)

    def cookies_query(self, userid):
        mycol = self.mydb["Cookies"]
        mydict = {"userId": userid}
        return mycol.find_one(mydict)

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
        mycol = self.mydb["User"]
        myquery = {"userId": userid}
        mydoc = mycol.find(myquery, {"userName": 1})
        if mydoc != None:
            username = mydoc["userName"]
            return username
        else:
            return ""
        return username

    def query_tagList(self):
        mycol = self.mydb["Tags"]
        tagList = mycol.find().pretty()
        return tagList

    def thinking_insert(self, createTime, userId, Title, ideaContent, classify, tags):
        mycol = self.mydb["Ideas"]
        mycol.insert({"createTime": createTime, "userId": userId, "Title": Title, "ideaContent": ideaContent
                         , "classify": classify, "tags": tags})

    def publish_insert(self, parentId, createTime, type):
        mycol = self.mydb["Publish"]
        mycol.insert({"parentId": parentId, "createTime": createTime, "type": type})

    def article_insert(self, createTime, userId, Title, subTitle, articleContent, classify, tags):
        mycol = self.mydb["Articles"]
        mycol.insert({"createTime": createTime, "userId": userId, "Title": Title,
                      "subTitle": subTitle, "articleContent": articleContent,
                      "classify": classify, "tags": tags})
