import hashlib
import json
from flask import request, make_response


def md5(user_name):
    md5 = hashlib.md5()
    md5.update(user_name.encode(encoding='UTF-8'))
    userid = md5.hexdigest()
    return userid


def aid():
    res = json.loads(request.get_data(as_text=True))
    aid = res['aid']
    return aid