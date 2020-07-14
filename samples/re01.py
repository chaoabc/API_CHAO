#!/usr/bin/env python
# encoding: utf-8
# @author: miaoxiaochao
# @file: re01.py
# @time: 2020/7/12 3:37 下午
#@desc:
import re

a2 ={"token":"12345"}
a1 ='{"access_token":${token}}'


# group()方法得到匹配的字符串,如果字符串没有匹配，则返回None
# value = re.match( 'class\d8' , 'class58' ).group()
# print( value )
# #
# value = re.findall('\\${\w+}',a1)[0]
# print( value)
# value2 =a1.replace(value,'"%s"'%a2.get(value[2:-1]))
# print(value2)
#
# #创建正则表达式对象
# str_c = re.compile('class\d8')
# #group()方法得到匹配的字符串,如果字符串没有匹配，则返回None
# value = str_c.match('class58').group()
# print( value )
#
#
# #创建正则表达式对象
# str_c = re.compile('\d8')
#
# value = str_c.search('class58').group()
# print( value )

print(eval('66+72')) # 把字符串解析成66+72的结果
print( eval("{'name':'linux','age':18}") ) # 把字符串转为字典
print( eval("[[1,2], [3,4], [5,6], [7,8], [9,0]]") ) # 把字符串转为列表
print(eval("{'name':'linux','age':age}",{"age":18})) # 传递globals参数值为{“age”:18}

age=18
print(eval("{'name':'linux','age':age}",{"age":20},locals())) # 传递locals参数

import ast

print( ast.literal_eval("{'name':'linux','age':18}") )
print( ast.literal_eval("[[1,2], [3,4], [5,6], [7,8], [9,0]]") )