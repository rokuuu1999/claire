from flask import Flask
from flask import request
import pymysql
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
        db = pymysql.connect(host="localhost",user= "root",password= "qq229574683", database="clay")
        cursor = db.cursor()
        sql = 'select * from user '
        res = cursor.execute(sql)
        data = cursor.fetchall()
        if request.form['username'] == data :
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
        db = pymysql.connect(host="localhost", user="root", password="qq229574683", database="clay")
        cursor = db.cursor()
        user_name = request.form['username']
        user_email = request.form['email']
        user_password = request.form['password']
        user_repassword = request.form['repassword']
        if user_repassword == user_password:
            sql = "INSERT INTO USER , VALUES('%s','%s','%s')" (user_name,user_email,user_password)
            db.close
            return '200okokokokk'
        else:
            return 'flase'