import pytest
import requests
from getToken.login import user_login
from readExcel.readExcel import read_excel
import json

data = list(zip(read_excel('路径'), read_excel('传参')))

@pytest.mark.parametrize("path, json_str", data)
def test_api(path, json_str):
    host = "http://api.redmou.com"

    url = host + path

    if json_str != '':
        json_dict = json.loads(json_str)  # 读取到的是str类型，转化成字典类型
    elif json_str == '':  # 如果这种情况不做处理会报错
        json_dict = ''

    token = user_login(1).front_get_token()
    headers = {"token": token}

    res = requests.post(url=url, json=json_dict, headers=headers)
    assert res.status_code == 200
    result = res.json()
    assert result['code'] == 0
    assert result['msg'] == 'ok'
    assert result['data'] is not None
    # print(res.json())  # 接口的返回json