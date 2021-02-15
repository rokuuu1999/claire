import json
from app import app, database
from flask import request,make_response
from datetime import datetime
from datetime import timedelta
import hashlib

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 不用明白为什么，暂时这么用

        res = json.loads(request.get_data(as_text=True))

        user_name = res['username']
        user_email = res['email']
        user_password = res['password']

        print(user_email)


        if database.login(user_name) == user_password:
            resp = make_response("success")
            md5 = hashlib.md5()
            md5.update(resp.encode('utf-8'))
            saltcookies = md5.hexdigest(user_name)
            resp.set_cookie('id','hanqi',saltcookies,amax_age = 3600)
            database.cookies(resp)
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

@app.route('/article')
    #acticle

@app.route('/home', methods = 'GET')
def home():
    if request.method == 'GET' :
        res = json.loads(request.get_data(as_text=True))
        article_time = res['datetime']

