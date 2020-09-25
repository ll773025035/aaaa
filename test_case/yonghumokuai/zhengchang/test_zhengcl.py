import random

from tools.api import request_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

def test_signup(pub_data):
    pub_data["username"] = "自动生成 字符串 1,5 数字 fasec"
    pub_data["pwd"] = "自动生成 字符串 2,5 数字 xcvsw"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户注册'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "注册成功"  # 预期结果
    json_data='''{
  "phone": "自动生成 手机号",
  "pwd": "${pwd}",
  "rePwd": "${pwd}",
  "userName": "${username}"
}'''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


def test_login(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "登录成功"  # 预期结果
    json_data='''{
  "pwd": "${pwd}",
  "userName": "${username}"
}'''

    json_path = [{"token":"$['data']['token']"}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_recharge(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '账户充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "充值成功"  # 预期结果
    json_data='''{
  "accountName": "${username}",
  "changeMoney": "自动生成 数字 20000,800000"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_getAccInfo(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '查询单个账户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_getBills(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询用户流水'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_charge(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '扣款测试'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/charge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "扣款成功"  # 预期结果
    json_data='''{
  "accountName": "${username}",
  "changeMoney": 66666
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_getAccInfo1(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '查询单个账户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_getBills1(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询用户流水'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)



def test_withdraw(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "提现成功"  # 预期结果
    json_data='''{
  "accountName": "${username}",
  "cardNo": "自动生成 字符串 10，17 数字 2",
  "changeMoney": 88888
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_getAccInfo2(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '查询单个账户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_getBills2(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询用户流水'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "查询成功"  # 预期结果
    params={'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

def test_accLock(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '冻结账户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accLock"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "账户冻结成功"  # 预期结果
    data={'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_recharge1(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '账户充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "该账户正处在冻结状态，无法充值"  # 预期结果
    json_data='''{
  "accountName": "${username}",
  "changeMoney": "自动生成 数字 20000,800000"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_withdraw1(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "该账户正处在冻结状态，无法提现"  # 预期结果
    json_data='''{
  "accountName": "${username}",
  "cardNo": "自动生成 字符串 10，17 数字 2",
  "changeMoney": 88888
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_charge1(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '扣款测试'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/charge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "扣款成功"  # 预期结果
    json_data='''{
  "accountName": "${username}",
  "changeMoney": 66666
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_accUnLock(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '解冻账户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accUnLock"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "账户解冻成功"  # 预期结果
    data={'accountName': '${username}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_recharge2(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '账户充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "充值成功"  # 预期结果
    json_data='''{
  "accountName": "${username}",
  "changeMoney": "自动生成 数字 20000,800000"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_withdraw2(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "账户模块"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = "提现成功"  # 预期结果
    json_data='''{
  "accountName": "${username}",
  "cardNo": "自动生成 字符串 10，17 数字 2",
  "changeMoney": 88888
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
