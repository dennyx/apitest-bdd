#!/usr/bin/env python
# -- coding=utf-8 --

'''
测试step
'''

from behave import when, then, given
from hamcrest import *
from utils.http_manager import make_get_request, make_post_request, make_put_request
import json
from urls.demo import URLS

import logging

@when('我发送请求去获取待办列表')
def get_todo_list(context):
    '''
    发送请求，获取数据
    '''
    resp = make_get_request(URLS["BASE_URL"])
    logging.info(resp)

@then('我应该收到对应的列表信息')
def check_todo_list_data(context):
    '''
    查看返回的基本数据
    '''
    assert_that('1', '1', '待调整')

@when('我发送请求去获取待办详情，参数如下')
def get_todo_detail(context):
    '''
    发送请求，获取数据
    '''
    params = json.loads(context.text)
    resp = make_get_request(URLS["BASE_URL"],params=params)
    logging.info(resp)

@then('我应该收到对应的待办详情')
def check_todo_detail(context):
    '''
    查看返回的基本数据
    '''
    assert_that('1', '1', '待调整')

@when('我发送请求去新增待办事项，参数如下')
def add_todo(context):
    '''
    发送请求，获取数据
    '''
    data = json.loads(context.text)
    resp = make_post_request(URLS["BASE_URL"], data=data)
    logging.info(resp)

@then('我应该新增成功')
def check_add_todo(context):
    '''
    查看返回的基本数据
    '''
    assert_that('1', '1', '待调整')

@when('我发送请求去修改待办事项，参数如下')
def update_todo(context):
    '''
    发送请求，获取数据
    '''
    data = json.loads(context.text)
    logging.info("data.params as %s" % data['params'])
    logging.info("data.data as %s" % data['data'])
    resp = make_put_request(URLS["BASE_URL"], params=data['params'], data=data['data'])
    logging.info(resp)

@then('我应该修改成功')
def check_update_todo(context):
    '''
    查看返回的基本数据
    '''
    assert_that('1', '1', '待调整')

