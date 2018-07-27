"""
自动化测试执行脚本
1. 执行测试用例
1.1 默认执行所有的测试用例
1.2 具体执行哪些测试用例，用behave.ini来进行控制
2. 生成测试报告
3. 发送通知：邮件、企业微信

TODO 增加定时任务
"""

import logging
import logging.config
import subprocess
import schedule
from datetime import datetime

from config import BASE_CONFIG
from utils.common import check_if_file_exists
from utils.Notifier.EmailNotifier import EmailNotifier
from utils.Notifier.WXWorkNotifier import WWorkNotifier

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },
    "handlers": {
        "default": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": 'qa_run.log',
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

logging.config.dictConfig(LOGGING_CONFIG)

class ZHQARunner(object):

    def __init__(self):
        self.run_result = {}

    def run(self):
        """
        增加为定时任务
        """
        if BASE_CONFIG['SCHEDULE']['ON']:
            schedule.every().day.at(BASE_CONFIG['SCHEDULE']['DAILY_SCHEDULE_TIME']).do(self.main)
            while True:
                schedule.run_pending()
        else:
            self.main()

    def main(self):
        """
        1. 执行测试用例
        1.1 默认执行所有的测试用例
        1.2 具体执行哪些测试用例，用behave.ini来进行控制
        2. 生成测试报告
        3. 发送通知：邮件、企业微信
        """
        self.__run_cases()
        self.__format_run_result()
        self.__notify()
        self.__check_and_rerun()
        # self.__allure_serve()

    def __check_and_rerun(self):
        """
        针对失败的测试用例，重新执行
        判断是否有失败的测试用例，以是否存在rerun_failing.features文件为准
        对应命令 behave '@rerun_failing.features'
        重新执行后，需要将内容更新到报告中
        """
        if BASE_CONFIG['RERUN']['ON'] and check_if_file_exists(BASE_CONFIG['RERUN']['RERUN_FILE_PATH']):
            logging.info("重新执行-准备针对失败的测试用例，进行重新执行")
            rerun_result = subprocess.getstatusoutput("behave '@%s'" % BASE_CONFIG['RERUN']['RERUN_FILE_NAME'])
            rerun_result_str = rerun_result[1]
            logging.info("重新执行-失败用例执行成功，结果为%s" % rerun_result_str)

    def __allure_serve(self):
        """
        启动allure serve服务
        需要考虑关闭相应的进程
        """
        subprocess.run('allure serve report')

    def __run_cases(self):
        """
        执行测试用例
        """
        logging.info("准备开始执行测试")
        run_result_origin = subprocess.getstatusoutput('behave -f allure_behave.formatter:AllureFormatter -o report ./features/workbench/workbench.feature')
        self.run_result = run_result_origin[1]
        logging.info("测试执行结果为\n%s" % self.run_result)

    def __format_run_result(self):
        """
        格式化测试执行结果
        1 feature passed, 0 failed, 0 skipped
        4 scenarios passed, 0 failed, 0 skipped
        9 steps passed, 0 failed, 0 skipped, 0 undefined
        Took 0m0.773s
        """
        result_origin = self.run_result.split('\n')
        format_result = {
            '测试场景': {
                '成功': '0',
                '失败': '0',
                '跳过': '0'
            },
            '测试用例': {
                '成功': '0',
                '失败': '0',
                '跳过': '0'
            },
            '测试步骤': {
                '成功': '0',
                '失败': '0',
                '跳过': '0'
            },
            '执行时间': ''
        }
        for line in result_origin:
            key = ''
            if 'feature passed' in line:
                key = '测试场景'
            elif 'scenarios passed' in line:
                key = '测试用例'
            elif 'steps passed' in line:
                key = '测试步骤'
            elif 'Took' in line:
                key = '执行时间'
            if key != '':
                if key == '执行时间':
                    format_result['执行时间'] = line.split(' ')[1]
                else:
                    temp_str = line.split(',')
                    format_result[key]['成功'] = temp_str[0].strip(' ').split(' ')[0]
                    format_result[key]['失败'] = temp_str[1].strip(' ').split(' ')[0]
                    format_result[key]['跳过'] = temp_str[2].strip(' ').split(' ')[0]
        self.run_result = format_result
        logging.info('测试执行结果为\n%s' % self.run_result)

    def __notify(self):
        """
        发送通知
        """
        logging.info("准备发送邮件通知")
        EmailNotifier().send_notify(self.run_result)
        logging.info("成功发送邮件通知")
        logging.info("准备发送企业微信通知")
        WWorkNotifier().send_notify(self.run_result)
        logging.info("成功发送企业微信通知")

if __name__ == "__main__":
    ZHQARunner().run()