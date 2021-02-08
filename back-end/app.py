from flask import Flask
from flask import request
import pymysql
from db import *
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':


        sql = 'select * from user '
        res = cursor.execute(sql)
        data = cursor.fetchall()
        if request.form['username'] == data:
            if request.form['mail'] == data:
                if request.form['password'] == data:
                    cursor.close()
                    db.close()
                    return '200ok'
        else:
            return "false"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form['username']
        user_email = request.form['email']
        user_password = request.form['password']
        user_repassword = request.form['repassword']
        cursor = db.cursor()
        data = cursor.fetchall()
        if user_repassword == user_password:
            sql = "INSERT INTO USER , VALUES('%s','%s','%s')" (user_name,user_email,user_password)
            db.close

            cursor.execute('sql')
            db.commit()
            return '200okokokokk'
        else:
            return 'flase'