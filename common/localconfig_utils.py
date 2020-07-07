#!/usr/bin/env python
# encoding: utf-8
# @author: miaoxiaochao
# @file: localconfig_utils.py
# @time: 2020/7/7 8:57 下午
#@desc:

import os
import configparser

current_path =os.path.dirname(__file__)
config_path =os.path.join(current_path,'..','config/config.ini')
# print(config_path)

class LocalConfigUtils():
    def __init__(self,config_path =config_path):
        self.cfg=configparser.ConfigParser()
        self.cfg.read(config_path)             #使用configparser方法读取配置文件


    @property     #将方法变为属性方法
    def URL(self):
        url_value =self.cfg.get('default','url')
        return url_value

    @property
    def LOG_PATH(self):
        log_path_value = self.cfg.get('path', 'LOG_PATH')
        return log_path_value

    @property
    def REPORTS_PATH(self):
        reports_path_value = self.cfg.get('path', 'REPORTS_PATH')
        return reports_path_value

    @property
    def LOG_LEVEL(self):
        log_level_value = int( self.cfg.get('log', 'LOG_LEVEL'))
        return log_level_value

    @property
    def CASE_DATA_PATH(self):
        case_data_path_value = self.cfg.get('path', 'CASE_DATA_PATH')
        return case_data_path_value


local_config =LocalConfigUtils()


if __name__=='__main__':
    print(local_config.REPORTS_PATH)       #cfg.reports_path


