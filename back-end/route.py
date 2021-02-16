import json
from app import app, database
from flask import request, make_response
from function import md5
import time

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 不用明白为什么，暂时这么用

        res = json.loads(request.get_data(as_text=True))

        user_name = res['username']
        user_email = res['email']
        user_password = res['password']
        data = database.login(user_name)
        if data[0] == user_password:
            outcome = {"id":data[1],"authroity":data[2],"avatarUrl":data[3]}
            resp = make_response(outcome)
            userid = md5(user_name)
            timeout = time.time() + 60 * 60 * 24
            resp.set_cookie('userid', userid, expires=timeout)  # , domain="localhost")
            database.cookies(userid,timeout)

            return resp
        else:
            return "fail"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 不用明白为什么
        res = json.loads(request.get_data(as_text=True))
        print(res)
        user_name = res['username']
        user_email = res['email']
        user_password = res['password']
        user_repassword = res['repassword']

        if user_repassword == user_password:
            database.register(user_name, user_email, user_password)
            return 'ok'
        else:
            return 'fail'



# @app.route('/article')
# acticle

@app.route('/home', methods=['GET'])
def home():
    if request.method == 'GET':
        res = json.loads(request.get_data(as_text=True))
        article_time = res['datetime']
