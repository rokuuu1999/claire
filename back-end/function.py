import hashlib
import json
from flask import request, make_response


def md5(private_key):
    md5 = hashlib.md5()
    md5.update(private_key.encode(encoding='UTF-8'))
    userid = md5.hexdigest()
    return userid
