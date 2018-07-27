"""
发送邮件
"""


import logging
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime

from config import BASE_CONFIG
from .email_template import EMAIL_TEMPLATE

class EmailNotifier(object):

    def __init__(self):
        self.in_usage = BASE_CONFIG['NOTIFY']['EMAIL']['ON']
        self.smtp_host = BASE_CONFIG['NOTIFY']['EMAIL']['SMTP_HOST']
        self.smtp_port = BASE_CONFIG['NOTIFY']['EMAIL']['SMTP_PORT']
        self.sender_email = BASE_CONFIG['NOTIFY']['EMAIL']['SEND_USER_EMAIL']
        self.sender_passwd = BASE_CONFIG['NOTIFY']['EMAIL']['SEND_USER_PASSWD']
        self.default_user = BASE_CONFIG['NOTIFY']['EMAIL']['DEFAULT_USER']
        self.target_user = BASE_CONFIG['NOTIFY']['EMAIL']['TARGET_USER']
        self.serve_url = BASE_CONFIG['NOTIFY']['SERVER_URL']

    def __gen_email_content(self, run_result, timeinfo):
        """
        根据执行结果，生成html内容
        """
        html_content = EMAIL_TEMPLATE % (timeinfo, run_result['测试用例']['成功'], run_result['测试用例']['失败'], run_result['测试用例']['跳过'], run_result['执行时间'])
        return html_content
    
    def send_notify(self, run_result):
        """
        发送邮件
        """
        logging.info("邮件通知-准备发送邮件")
        current_time = datetime.now().strftime('%Y-%m-%d')
        current_time_detail = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mail_msg = self.__gen_email_content(run_result, current_time_detail)
        message = MIMEText(mail_msg, 'html', 'utf-8')
        self.target_user.extend(self.default_user)
        message['From'] = Header("ZHQA<%s>" % (self.sender_email), 'utf-8')
        message['To'] =  Header("%s" % ','.join(self.target_user), 'utf-8')
        subject = '自动化测试报告%s' % current_time
        message['Subject'] = Header(subject, 'utf-8')
        try:
            server = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)
            server.login(self.sender_email, self.sender_passwd)
            logging.info("邮件通知-准备发送邮件给%s" % self.target_user)
            server.sendmail(self.sender_email,self.target_user , message.as_string())
            logging.info("邮件通知-邮件发送成功")
        except smtplib.SMTPException:
            logging.error("邮件通知-Error: 无法发送邮件")
