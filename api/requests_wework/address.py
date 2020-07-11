from api.requests_wework.base_api import BaseApi
from api.requests_wework.wework import WeWork

class Address(BaseApi):

    def __init__(self):
        secret = "2MXedRgNClgNrGZ3Vz3A3jWVqRU-zEHBqDbS6Qq4ChY"
        self.token = WeWork().get_token(secret)


    def create(self, userid, name, mobile):
        # 添加成员
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1]
            }
        }
        return self.send(data)


    def update(self, userid, name, mobile):
        # 更新成员
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
            }
        }
        return self.send(data)


    def delete(self, userid):
        # 删除成员
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": self.token,
                "userid": userid
            }

        }
        return self.send(data)

