import requests
from readExcel.readExcel import chose_role


class Massage():
    def __init__(self, path, username, email, password, role):
        self.path = path
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def front_get_token(self): # 前台登录（app接口登录）
        host = "http://api.redmou.com"
        url = host + self.path
        json = {
            "nickname": self.username,
            "email": self.email,
            "password": self.password,
            "firebaseToken": "string"
        }
        res = requests.post(url=url, json=json)
        token = res.json().get("data").get("token") # 从响应体中获取 token
        return token

    def manager_get_token(self): # 后台登录（管理后台登录）
        # 登录端 11礼品卡求购端; 12提现处理端; 为null代表是后台管理
        host = "http://api.redmou.com"
        url = host + self.path
        json = {
            "client": self.role,
            "loginName": self.username,
            "password": self.password
        }
        res = requests.post(url=url, json=json)
        token = res.json().get("data").get("token") # 从响应体中获取 token
        return token


def user_login(role): # 获取用户信息并实例化信息类
    user_massage = chose_role('角色', role)
    user = Massage(user_massage[0],
                   user_massage[1],
                   user_massage[2],
                   user_massage[3],
                   user_massage[4])
    return user

if __name__ == '__main__':
    #user = user_login(1)
    print(user_login(1).get_token())
