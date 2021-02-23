import hashlib
from qiniu import Auth
from setting import AK, SK


def md5(private_key):
    md5 = hashlib.md5()
    md5.update(private_key.encode(encoding='UTF-8'))
    userid = md5.hexdigest()
    return userid


class kodo:
    def __init__(self):
        kodo = Auth(AK, SK)
