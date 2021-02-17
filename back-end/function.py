import hashlib
import json
from flask import request, make_response


def md5(user_name):
    md5 = hashlib.md5()
    md5.update(user_name.encode(encoding='UTF-8'))
    userid = md5.hexdigest()
    return userid
