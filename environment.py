#!/usr/bin/env python
# -- coding=utf-8 --

"""
基本生命周期描述

before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.

before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.

before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.

before_tag(context, tag), after_tag(context, tag)

++++++++++++++++++++++++++++++++++++++++++++++++++++
run operation
before_all
for feature in all_features:
    before_feature
    for scenario in feature.scenarios:
        before_scenario
        for step in scenario.steps:
            before_step
                step.run()
            after_step
        after_scenario
    after_feature
after_all

"""

import logging
import logging.config

import allure
from allure_commons.types import AttachmentType

from config import BASE_CONFIG, LOGGING_CONFIG
from utils.common import clean_folders

from utils.database.db2.DB2Client import DB2Client
from utils.database.redis.RedisClient import RedisClient

logging.config.dictConfig(LOGGING_CONFIG)

def before_all(context):
    '''
    触发时间：整体测试开始前
    职责定义：
    1. 清理临时目录
    2. 检查测试环境
    3. 准备基础测试数据
    4. 建立全局连接，如数据库连接等
    '''
    # 清楚临时目录
    clean_temp_folder()
    # 初始化数据
    context.data = {}
    # 初始化连接
    init_db_conn(context)

def after_all(context):
    '''
    触发时间：整体测试结束后
    职责定义:
    1. 释放所有资源，如数据库连接等
    2. 清理此次测试执行，产生的脏数据
    3. 清理临时文件
    4. 整理报告，如邮件发送报告

    '''
    release_db_conn(context)

def before_feature(context, feature):
    '''
    触发时间：测试集开始前
    职责定义：
    1. 该测试集的测试环境准备
    '''
    pass


def before_tag(context, tag):
    '''
    触发时间： 有增加TAG的测试用例执行前
    备注： 如果TAG加在feature文件顶部，则表示该测试集中的所有测试用例都覆盖；如果有多个tag时，依次进行处理
    职责定义:
    1. 区分不同测试集、测试用例的测试环境、使用场景等，根据标记来进行特殊处理，如需要登录等
    2. 可以指定执行某种tag标记相关的测试集、测试用例，方便管理；如冒烟测试用例，回归测试用例，已知BUG等
    '''
    if tag == 'NEED_LOGIN':
        try:
            # do_login()
            pass
        except Exception as e:
            logging.exception("Error occured as %s" % e)
            raise Exception("Failed to login")


def after_tag(context, tag):
    '''
    触发时间： 有增加TAG的测试用例执行前
    备注： 如果TAG加在feature文件顶部，则表示该测试集中的所有测试用例都覆盖；如果有多个tag时，依次进行处理
    职责定义：
    1. 特殊处理行为后续处理
    '''
    if tag == 'NEED_LOGIN':
        try:
            # do_logout(context)
            pass
        except Exception as e:
            logging.exception("Error occured as %s" % e)
            raise Exception("Failed to logout")


def before_scenario(context, scenario):
    '''
    触发时间: 测试用例执行前
    职责:
    1. 测试用例执行前的基本处理，如环境重新初始化等
    '''
    pass


def after_scenario(context, scenario):
    '''
    触发时间: 测试用例执行后
    职责:
    1. 测试用例执行前的基本处理，如环境清理等
    2. 检查测试用例执行结果，如果不成功，则需要追加详细信息到报告中
    '''
    if scenario.status != 'passed':
        # allure中增加详细的错误描述信息
        pass

def clean_temp_folder():
    '''
    清除临时文件夹
    '''
    temp_folders = [
        BASE_CONFIG['REPORT_FOLDER'],
        BASE_CONFIG['ALLURE_REPORT_FOLDER'],
        BASE_CONFIG['TEMP_FOLDER'],
    ]
    clean_folders(temp_folders)

def init_db_conn(context):
    """
    增加数据库连接
    """
    if BASE_CONFIG['DB']['DB_CONNECT']:
        # 这里不使用反射，单独进行处理，以免在后续使用客户端的时候混乱
        # DB2
        context.db2_client = DB2Client()
        context.db2_client.connect_db()
        context.db2_client.check_db()
        # Redis
        context.redis_client = RedisClient()
        context.redis_client.connect_db()
        context.redis_client.check_db()

def release_db_conn(context):
    """
    释放数据库连接
    """
    if BASE_CONFIG['DB']['DB_CONNECT']:
        context.db2_client.close_db()
        context.redis_client.close_db()