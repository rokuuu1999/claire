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

    def cookies(self, userid,time):
        cursor = self.db.cursor()
        sql = "INSERT INTO COOKIES(userid,time) VALUES('%s',%s)  ON DUPLICATE KEY UPDATE time = time" % (userid,time)
        cursor.execute(sql)
        self.db.commit()

    def article(self,aid):
        cursor = self.db.cursor()
        sql = "SELECT AID,ARTICLETITLE,SUBTITLE,ARTICLECONTENT,USERID,TIME,COMMENTNUM,LIKENUM,CLASSIFY FROM ARTICLES WHERE AID = (%s)" % (aid)
        cursor.execute(sql)
        res = cursor.fetchone()
        return res

    def tags(self,aid):
        cursor = self.db.cursor()
        sql = "SELECT AID,TAG FROM TAGS WHERE aid=('%s')" % (aid)
        cursor.execute(sql)
        res = cursor.fetchall()
        return res

    def articleimg(self,aid):
        cursor = self.db.cursor()
        sql = "SELECT AID , IMG FROM ARTICLEIMG WHERE AID = ('%s')" % (aid)
        cursor.execute(sql)
        res = cursor.fetchone()
        return res

