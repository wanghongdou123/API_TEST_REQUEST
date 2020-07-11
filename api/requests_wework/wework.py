from api.requests_wework.base_api import BaseApi

class WeWork(BaseApi):
    def get_token(self, secret):
        # 获取 token
        corpid = "wwaf7b9d2f2c44ef08"
        corpsecret = secret
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        
        return self.send(data)["access_token"]