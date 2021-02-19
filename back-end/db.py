import pymysql
import datetime
import pymongo


# Python 面向对象写法
class db:
    def __init__(self):
        self.connect()

    def connect(self):
        self.myclient = pymongo.MongoClient("mongodb://root:rokuuu1999@121.4.74.77:27017/admin")
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
        mycol = self.mydb["user"]
        myquery = {"userId": userid}
        mydoc = mycol.find(myquery, {"userName": 1})
        username = mydoc
        return username

    def queryallelements(self, database_name):
        sql = "SELECT * FROM (%s)" % database_name
        elements = self.get_dict_data_sql(sql)
        return elements
