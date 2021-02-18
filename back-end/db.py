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
        # self.db = pymysql.connect(host="localhost", user="root", password="nothing0101.", database="test")

    def disconnect(self):
        self.db.disconnect()

    def login(self, username):
        cursor = self.db.cursor()
        sql = "select password,userid,userauthority,avatarUrl from user where username=('%s')" % (username)
        cursor.execute(sql)
        res = cursor.fetchone()

        return res

    def register(self, user_name, user_email, user_password):
        cursor = self.db.cursor()
        sql = "INSERT INTO USER(username,email,password) VALUES('%s','%s','%s')" % (
            user_name, user_email, user_password)
        cursor.execute(sql)
        self.db.commit()

    def cookies(self, userid, time):
        cursor = self.db.cursor()
        sql = "INSERT INTO COOKIES(userid,time) VALUES('%s',%s)  ON DUPLICATE KEY UPDATE time = time" % (userid, time)
        cursor.execute(sql)
        self.db.commit()

    def article(self, aid):
        cursor = self.db.cursor()
        sql = "SELECT AID,ARTICLETITLE,SUBTITLE,ARTICLECONTENT,CREATETIME,COMMENTNUM,LIKENUM,CLASSIFY FROM ARTICLES WHERE AID = (%s)" % (
            aid)
        cursor.execute(sql)
        res = cursor.fetchone()
        return res

    def tags(self, tid):
        cursor = self.db.cursor()
        sql = "SELECT AID,TAG FROM TAGS WHERE TID=('%s')" % (tid)
        cursor.execute(sql)
        res = cursor.fetchall()
        return res

    def articleimg(self, iid):
        cursor = self.db.cursor()
        sql = "SELECT AID , IMG FROM ARTICLEIMG WHERE IID = ('%s')" % (iid)
        cursor.execute(sql)
        res = cursor.fetchone()
        return res

    def queryusername(self, userid):
        cursor = self.cursor()
        sql = "SELECT USERNAME FROM USER WHERE USERID = ('%s')" % userid
        cursor.execute(sql)
        username = cursor.fetchone()
        return username

    def queryallelements(self, database_name):
        sql = "SELECT * FROM (%s)" % database_name
        elements = self.get_dict_data_sql(sql)
        return elements

    def get_index_dict(self, cursor):
        """
        获取数据库对应表中的字段名
        """
        index_dict = dict()
        index = 0
        for desc in cursor.description:
            index_dict[desc[0]] = index
            index = index + 1
        return index_dict

    def get_dict_data_sql(self, sql):
        """
        运行sql语句，获取结果，并根据表中字段名，转化成dict格式（默认是tuple格式）
        """
        cursor = self.db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        index_dict = self.get_index_dict(cursor)
        res = []
        for datai in data:
            resi = dict()
            for indexi in index_dict:
                resi[indexi] = datai[index_dict[indexi]]
            res.append(resi)
        return res
