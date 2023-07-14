import pytest
import requests
from getToken.login import user_login
from readExcel.readExcel import read_excel
import json

# sheet参数0为APP，1为管理后天，2为礼品卡，3为提现
data = list(zip(read_excel('路径', 1), read_excel('传参', 1)))

# APP登录
# token = user_login(1).front_get_token()

# 后台登录：null为管理后台，11为礼品卡，12为提现
token = user_login('').manager_get_token()

@pytest.mark.parametrize("path, json_str", data)
def test_api(path, json_str):
    host = "http://api.redmou.com"

    url = host + path

    if json_str != '':
        json_dict = json.loads(json_str)  # 读取到的是str类型，转化成字典类型
    elif json_str == '':  # 如果这种情况不做处理会报错
        json_dict = ''

    headers = {"token": token}

    res = requests.post(url=url, json=json_dict, headers=headers)
    assert res.status_code == 200
    result = res.json()
    assert result['code'] == 0
    assert result['msg'] == 'ok'
    assert result['data'] is not None
    # print(res.json())  # 接口的返回json