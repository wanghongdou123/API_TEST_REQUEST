import re
import pytest
import requests


@pytest.fixture(scope="session")
def test_token():
    # 获取 token
    corpid = "wwaf7b9d2f2c44ef08"
    corpsecret = "2MXedRgNClgNrGZ3Vz3A3jWVqRU-zEHBqDbS6Qq4ChY"
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    return res.json()["access_token"]


def test_get(userid, test_token):
    # 根据 user-id查询成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}")
    return res.json()


def test_create(userid, name, mobile, test_token):
    # 添加成员
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1],
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}",
                        json=data
                        )
    return res.json()


def test_update(userid, name, mobile, test_token):
    # 更新成员
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}",
                        json=data)
    return res.json()


def test_delete(userid, test_token):
    # 删除成员
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
    return res.json()


@pytest.mark.parametrize("userid, name, mobile",[("lisa1","丽莎1","13811110001")])
def test_all(userid, name, mobile, test_token):
    # 可能出现创建失败
    try:
        # 验证创建
        assert "created" == test_create(userid, name, mobile, test_token)["errmsg"]
    except AssertionError as e:
        print("12345")
        if "mobile existed" in e.__str__():
            print("111")
            print(e.__str__())
            print('222')
            # 如果手机号被使用了，找出使用手机号的userid,进行删除
            re_userid = re.findall(":(.*)'", e.__str__())[0]
            print(re_userid)
            print("333")
            assert "deleted" == test_delete(re_userid, test_token)["errmsg"]
            assert 60111 == test_get(re_userid, test_token)["errcode"]
            assert "created" == test_create(userid, name, mobile, test_token)["errmsg"]


    # 可能发生userid不存在异常
    assert name == test_get(userid, test_token)["name"]
    assert "updated" == test_update(userid,"xxxxxx",mobile, test_token)["errmsg"]
    assert "xxxxxx" == test_get(userid, test_token)["name"]
    assert "deleted" == test_delete(userid, test_token)["errmsg"]
    assert 60111 == test_get(userid, test_token)["errcode"]

