#!/usr/bin/env python
# encoding: utf-8
# @author: miaoxiaochao
# @file: xlutils_demo.py
# @time: 2020/7/25 3:27 下午
#@desc:


import os
import xlrd

from xlutils.copy import copy
excel_path = os.path.join(os.path.dirname(__file__),'test.xls')
print(excel_path)
wob = xlrd.open_workbook(excel_path,formatting_info=True)
mybook = copy(wob)
sheet = mybook.get_sheet(wob.sheet_names().index('Sheet1'))
sheet.write(1,1,20)
mybook.save()