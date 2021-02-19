import pymysql
import datetime
import pymongo


# Python 面向对象写法
class db:
    def __init__(self):
        self.connect()

    def connect(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["clay"]

    def login(self, username):
        mycol = self.mydb["user"]
        myquery = {"user": username}
        mydoc = mycol.find(myquery)
        res = mydoc
        return res

    def register(self, user_id, user_name, user_email, user_password):
        mycol = self.mydb["User"]
        mydict = {"userId": user_id, "userName": user_name, "email": user_email, "password": user_password}
        res = mycol.insert_one(mydict)

    def cookies(self, userid, time):
        mycol = self.mydb["Cookies"]
        mydict = {"userId": userid, "expireTime": time}
        res = mycol.insert_one(mydict)

    def cookies_query(self, userid):
        mycol = self.mydb["Cookies"]
        mydict = {"userId": userid}
        mydoc = mycol.find_one(mydict)
        res = mydoc
        return res

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

    def publish_query_nskips(self):
        mycol = self.mydb["Publish"]
        mydoc = mycol.search_set.find()
        res = mydoc
        return res
    def queryusername(self, userid):
        mycol = self.mydb["user"]
        myquery = {"userId": userid}
        mydoc = mycol.find(myquery, {"userName": 1})
        username = mydoc
        return username

    def queryallelements(self, database_name):
        sql = "SELECT * FROM (%s)" % database_name
        elements = self.get_dict_data_sql(sql)
        return elements
