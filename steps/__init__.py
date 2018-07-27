#!/usr/bin/env python
# -- coding=utf-8 --

"""
自定义预处理类型
"""

from behave import register_type
from parse import with_pattern
import json

def parse_number(text):
    """
    字符串转数字
    """
    return int(text)
register_type(Number=parse_number)

def parse_json(text):
    """
    字符串转json
    """
    return json.loads(text)
register_type(JSON=parse_json)


def parse_list(text):
    """
    字符转数组，逗号分隔
    """
    return text.split(",")

def parse_dic(text):
    """
    字符转字典
    """
    return eval(text)

@with_pattern(r"a\s+")
def parse_word_a(text):
    """
    任意文本
    """
    return text.strip()

# -- REGISTER: User-defined type converter (parse_type).
register_type(Number=parse_number)
register_type(List=parse_list)
register_type(Dic=parse_dic)
register_type(a_=parse_word_a)