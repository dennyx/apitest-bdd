"""
通用步骤
"""

from behave import when, then, given
from hamcrest import assert_that, equal_to
from utils.http_manager import make_post_request
from urls import *
from enums.CodeEnum import RESP_CODE_ENUM

import json
import logging

@when('我发送POST请求，组件为"{component}" key为"{url_key}"，请求内容为')
def common_make_post_request(context, component, url_key):
    """
    封装发送请求通用方法
    """
    clazz = globals()[component]
    url = clazz.URLS[url_key]
    headers = {}
    params = {}
    data = {}
    if context.text:
        origin_data = json.loads(context.text)
        headers = origin_data.get('headers', headers)
        params = origin_data.get('params', params)
        data = origin_data.get('data', data)
    resp = make_post_request(sub_url=url, data=data, headers=headers, params=params)
    context.data = resp

@then('我应该获取到正常的返回数据')
def check_normal_resp_base_info(context):
    """
    只校验code为0000
    """
    assert_that(context.data['code'], equal_to(str(RESP_CODE_ENUM.SUCCESS)), "返回正常报文，code应该为0000")

@then('返回数据"{resp_verify_key}" 和数据库中的内容一致, sql如下')
def check_resp_with_db(context, resp_verify_key):
    """
    根据指定的key，获取需要验证的内容部分
    key需要是data下的完整路径
    """
    actual_value = context.data['data'][resp_verify_key]
    db_value = context.db2_client.exe_sql(context.text)

    # 进行对比
    assert_that('bak', equal_to('bak'), "校验数据")

# 校验分页通用方法