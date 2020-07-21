#!/usr/bin/env python
# encoding: utf-8
# @author: miaoxiaochao
# @file: s1_demo.py
# @time: 2020/7/19 8:53 上午
#@desc:

from common.requests_utils import RequestsUtils

#获取所有用户标签
test_data1 =[
    {'测试用例编号': 'case02', '测试用例名称': '获取access_token值', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口',
     '请求方式': 'get', '请求地址': '/cgi-bin/token',
     '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}',
     '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配',
     '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
    {'测试用例编号': 'case02', '测试用例名称': '正确获取所有用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '获取所有标签接口', '请求方式': 'get',
     '请求地址': '/cgi-bin/tags/get', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '', '取值方式': '无', '传值变量': '',
     '取值代码': '', '期望结果类型': '正则匹配', '期望结果': '{"id":(.+?),"name":"蜻蜓队长"'}

]

#新增标签
test_data2 =[
    {'测试用例编号': 'case01', '测试用例名称': '获取access_token', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
    {'测试用例编号': 'case02', '测试用例名称': '测试能否成功新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post',
     '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag" : {"name" : "008"}}', '取值方式': '无', '传值变量': '',
     '取值代码': '', '期望结果类型': '正则匹配', '期望结果': '{"tag":{"id":(.+?),"name":"008"}}'},
             ]

#修改标签
test_data3 =[
    {'测试用例编号': 'case01', '测试用例名称': '获取access_token', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口',
     '请求方式': 'get', '请求地址': '/cgi-bin/token',
     '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}',
     '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token','期望结果类型': '正则匹配',
     '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
    {'测试用例编号': 'case02', '测试用例名称': '修改用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '修改标签接口', '请求方式': 'post',
     '请求地址': '/cgi-bin/tags/update', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{ "tag" : {"id" : 571,"name" : "008vv" }}', '取值方式': '无', '传值变量': '',
     '取值代码': '', '期望结果类型': '正则匹配', '期望结果': '{"tag":{"id":(.+?),"name":"008vv"}}'}


]

#删除标签
test_data4 =[
    {'测试用例编号': 'case01', '测试用例名称': '获取access_token', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
    {'测试用例编号': 'case02', '测试用例名称': '删除用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '删除标签接口', '请求方式': 'post',
     '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"id" : 2}}', '取值方式': '无', '传值变量': '',
     '取值代码': '', '期望结果类型': '正则匹配', '期望结果': '{"errmsg":"ok"'}
             ]




RequestsUtils().request_by_step(test_data1)