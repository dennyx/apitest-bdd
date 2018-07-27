#!/usr/bin/env python
# -- coding=utf-8 --

'''
http请求工具类
'''

import requests
from config import BASE_CONFIG
import logging
import json

def make_get_request(sub_url, headers = {}, params = {}):
    '''
    Get请求
    '''
    url = BASE_CONFIG['BASE_URL'] + sub_url
    logging.info("GET请求准备发送, url as %s, headers as %s, params as %s " % (url, headers, params))
    result = requests.get(url=url, params=params, headers = headers)
    format_result = result.content.decode('UTF-8')
    logging.info("GET请求成功发送, url as %s, headers as %s, params as %s, result as %s" % (url, headers, params, format_result))
    return format_result

def make_post_request(sub_url, data='', headers = {}, params = {}):
    '''
    Post请求
    '''
    url = BASE_CONFIG['BASE_URL'] + sub_url
    logging.info("POST请求准备发送, url as %s, headers as %s, params as %s, data as %s" % (url, headers, params, data))
    result = requests.post(url=url, data=json.dumps(data), headers = headers, params = params)
    format_result = json.loads(result.content)
    logging.info("POST请求成功发送, url as %s, headers as %s, params as %s, data as %s, result as %s" % (url, headers, params, data, format_result))
    return format_result

def make_put_request(sub_url, data='', headers = {}, params = {}):
    '''
    Put请求
    '''
    url = BASE_CONFIG['BASE_URL'] + sub_url
    logging.info("PUT请求准备发送, url as %s, headers as %s, params as %s, data as %s" % (url, headers, params, data))
    result = requests.put(url=url, data=json.dumps(data), headers = headers, params = params)
    format_result = result.content.decode('UTF-8')
    logging.info("PUT请求成功发送, url as %s, headers as %s, params as %s, data as %s, result as %s" % (url, headers, params, data, format_result))
    return format_result

def make_delete_request(sub_url, headers = {}, params = {}):
    '''
    Delete请求
    '''
    url = BASE_CONFIG['BASE_URL'] + sub_url
    logging.info("DELETE请求准备发送, url as %s, headers as %s, params as %s " % (url, headers, params))
    result = requests.get(url=url, params=params, headers = headers)
    format_result = result.content.decode('UTF-8')
    logging.info("DELETE请求成功发送, url as %s, headers as %s, params as %s, result as %s" % (url, headers, params, format_result))
    return format_result