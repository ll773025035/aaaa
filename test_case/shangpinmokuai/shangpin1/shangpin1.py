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
json_path = [{"token":"$['data']['token']"}]

def test_addProd(pub_data):
    pub_data["code"] = "自动生成 字符串 3,10 数字"
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '增加产品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "创建产品成功"  # 预期结果
    json_data='''{
  "brand": "小米",
  "colors": [
    "string"
  ],
  "price": "自动生成 数字 99,8888",
  "productCode": "${code}",
  "productName": "小米",
  "sizes": [
    "32G512G"
  ],
  "type": "手机"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_soldOut(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '下架'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    headers = {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'productCode': '${code}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_toPreSale(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '预售'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/toPreSale"  # 接口地址
    headers = {"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'productCode': '${code}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_getSkuByProdCode(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': 'YSL008'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)


