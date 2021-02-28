import hashlib
from qiniu import Auth, put_file
from setting import AK, SK


def md5(private_key):
    md5 = hashlib.md5()
    md5.update(private_key.encode(encoding='UTF-8'))
    userid = md5.hexdigest()
    return userid


class qiniu:
    def __init__(self):
        self.kodo = Auth(AK, SK)
        self.bucket_name = 'siegelion'

    def upload(self, fileName):
        # 生成上传 Token，可以指定过期时间等
        token = self.kodo.upload_token(self.bucket_name, fileName, 3600)
        localFile = './tmp/' + fileName
        ret, info = put_file(token, fileName, localFile)
        return ret["key"]
