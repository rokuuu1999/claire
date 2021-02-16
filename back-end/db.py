import pymysql
import datetime


# Python 面向对象写法
class db:
    def __init__(self):
        self.db = None
        self.cursor = None
        self.connect()

    def connect(self):
        self.db = pymysql.connect(host="localhost", user="root", password="qq229574683", database="clay")
        #self.db = pymysql.connect(host="localhost", user="root", password="nothing0101.", database="test")

    def disconnect(self):
        self.db.disconnect()

    def login(self, username):
        cursor = self.db.cursor()
        sql = "select password,id,authority,avatarUrl from user where username=('%s')" % (username)
        cursor.execute(sql)
        res = cursor.fetchone()

        return res

    def register(self, user_name, user_email, user_password):
        cursor = self.db.cursor()
        sql = "INSERT INTO USER(username,email,password) VALUES('%s','%s','%s')" % (
            user_name, user_email, user_password)
        cursor.execute(sql)
        self.db.commit()

    def cookies(self, userid):
        cursor = self.db.cursor()
        sql = "INSERT INTO COOKIES(userid) VALUES('%s')" % (userid)
        cursor.execute(sql)
        self.db.commit()


class article:

    def __init__(self):
        self.db = None
        self.cursor = None
        self.connect()

    def connect(self):
        self.db = pymysql.connect(host="localhost", user="root", password="qq229574683", database="clay")
        # self.db = pymysql.connect(host="localhost", user="root", password="nothing0101.", database="test")

    def disconnect(self):
        self.db.disconnect()

    def Article(self, user_name, user_time, tag):
        cursor = self.db.cursor()
        sql = """SELECT """
        cursor.execute(sql)
        res = cursor.fetchone()
        return res[0]
