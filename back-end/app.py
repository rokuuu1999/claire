from flask import Flask
from db import db
from flask_cors import *

app = Flask(__name__)
# 允许跨域
CORS(app, supports_credentials=True)

database = db()
from route import *
