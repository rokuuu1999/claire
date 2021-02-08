import pymysql
db = pymysql.connect(host="localhost", user="root", password="qq229574683", database="clay")
cursor = db.cursor()
res = cursor.execute(sql)