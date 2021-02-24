import requests




# class Url_weixin():
#     accesss_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET'


def test_weixin_request():
    #获取token
    corpid = 'wwe3dfe4e68715330f'
    corpsecret = '7gMnEOxBGenAHxN6kBGyUP8YXJkkQsvRKRVJQPLA90U'
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
    r =requests.get(url)
    print(r.json())
    cc_access_token = r.json()['access_token']
    print(cc_access_token)
    assert r.json()

    #创建成员
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={cc_access_token}'
    cc_json = {
    "userid": "ezer",
    "name": "伊泽瑞尔",
    "alias": "小黄人儿",
    "mobile": "+86 13800000080",
    "department": [1]}
    r = requests.post(url,json=cc_json)
    print(r.json())

    #读取成员接口
    userid = 'ezer'
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={cc_access_token}&userid={userid}'
    r = requests.get(url,)
    print(r.text)

    #更新成员信息
    url =f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={cc_access_token}'
    check_json = {
    "userid": "ezer",
    "name": "格雷福斯1",
    "department": [1],
    "mobile": "13800000080",}
    r = requests.post(url,json=check_json)
    print(r.json())

    #删除成员信息
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={cc_access_token}&userid=airuiliy'
    r = requests.get(url)
    print(r.json())