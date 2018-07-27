#!/usr/bin/env python
# -- coding=utf-8 --

'''
配置模板文件
各人需要根据config_template.py建立自己的config.py文件
'''

import os

current_path = os.path.dirname(os.path.realpath(__file__))

BASE_CONFIG = {
    # 基本的URL
    "BASE_URL": "http://127.0.0.1:5001",
    "DB": {
        "DB_CONNECT": True, # 临时参数，只有此参数打开时，才会在environment中增加数据库连接
        "INFO": {
            # 敏感信息，本应该放到.env文件中，后续进行调整
            "DB2": {
                "NAME": "db2_client",
                "HOST":'',
                "PORT": 50000,
                "USERNAME": '',
                "PASSWORD": '',
                "DB_NAME": '',
                "CONNECTION_NUM": 1 # 是否启用连接池，及对应的连接数
            },
            "REDIS": {
                "NAME": "redis_client",
                "HOST": '',
                "PORT": 6379,
                "USERNAME": '',
                "PASSWORD": '',
                "DB_NAME": 0,
                "CONNECTION_NUM": 1 # 是否启用连接池，及对应的连接数
            }
        }
    },
    # 报告目录
    "REPORT_FOLDER": os.path.join(current_path, "report"),
    # allure报告目录
    "ALLURE_REPORT_FOLDER": os.path.join(current_path, "allure_report"),
    # 临时文件目录
    "TEMP_FOLDER": os.path.join(current_path, "temp"),
    # 通知
    "NOTIFY": {
        # 邮件通知
        "EMAIL": {
            "ON": False,
            "SMTP_HOST": "",
            "SMTP_PORT": 465,
            "SEND_USER_EMAIL": "", # 发件人邮箱地址
            "SEND_USER_PASSWD": "", # 发件人邮箱密码
            "DEFAULT_USER": [""], # 默认接收人
            "TARGET_USER": [], # 接收人邮箱地址，多个的话，以逗号进行分隔
        },
        # 企业微信通知
        "WXWORK": {
            "ON": False,
            "DEFAULT_USER": "", # 默认接收人
            "TARGET_USER": "", # 接收人
            "TARGET_PARTY": "", # 接收群组
            "GET_TOKEN_URL": "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=",
            "SEND_MESSAGE_URL": "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=",
            "AGENT_ID": "",
            "CORP_ID": "",
            "CORP_SECRET": ""
        },
        # 测试结果对应的文件服务地址
        "SERVER_URL": ''
    },
    # 定时任务配置
    "SCHEDULE": {
        "ON": False,
        "DAILY_SCHEDULE_TIME": "00:00"
    },
    # 是否针对失败的用例进行重新执行
    "RERUN": {
        "ON": False,
        "TIMES": 1,
        "RERUN_FILE_NAME": "rerun_failing.features",
        "RERUN_FILE_PATH": os.path.join(current_path, "rerun_failing.features"),
    }
}

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            'format': '%(asctime)s [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },
    "handlers": {
        "default": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": 'credit_test.log',
            'mode': 'w+',
            "encoding": "utf8"
        },
    },
    "root": {
        'handlers': ['default'],
        'level': "DEBUG",
        'propagate': False
    }
}