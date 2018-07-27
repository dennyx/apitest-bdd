"""
发送企业微信通知

"""

from config import BASE_CONFIG
import logging
import json
import requests
from datetime import datetime

class WWorkNotifier(object):

    def __init__(self):
        self.in_usage = BASE_CONFIG['NOTIFY']['WXWORK']['ON']
        self.get_token_url = BASE_CONFIG['NOTIFY']['WXWORK']['GET_TOKEN_URL']
        self.send_message_url = BASE_CONFIG['NOTIFY']['WXWORK']['SEND_MESSAGE_URL']
        self.agent_id = BASE_CONFIG['NOTIFY']['WXWORK']['AGENT_ID']
        self.corp_id = BASE_CONFIG['NOTIFY']['WXWORK']['CORP_ID']
        self.corp_secret = BASE_CONFIG['NOTIFY']['WXWORK']['CORP_SECRET']
        self.target_user = '%s|%s'.rstrip('|') % (BASE_CONFIG['NOTIFY']['WXWORK']['DEFAULT_USER'], BASE_CONFIG['NOTIFY']['WXWORK']['TARGET_USER'])
        self.target_party = BASE_CONFIG['NOTIFY']['WXWORK']['TARGET_PARTY']
        self.serve_url = BASE_CONFIG['NOTIFY']['SERVER_URL']

    def send_notify(self, run_result):
        """
        发送通知
        """
        if not self.in_usage:
            logging.info("企业微信通知被禁用，不发送测试结果")
            return
        textcard = self.__gen_text_card(run_result)
        self.__sendmsg(textcard)
    
    def __get_access_token(self):
        access_token_url = "%s%s&corpsecret=%s" % (self.get_token_url, self.corp_id, self.corp_secret)
        try:
            res_data = requests.get(access_token_url)
            access_token = json.loads(res_data.content)["access_token"]
        except Exception as e:
            logging.error("企业微信通知-access_token获取超时，具体错误为\n%s" % str(e) )
            return None
        else:
            return access_token

    def __gen_text_card(self, run_result):
        """
        生成消息模板
        """
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        textcard = {
            "title" : "QA%s" % current_date,
            "description" : '''
                <div class=\"normal\">测试用例执行成功%s个</div>
                <div class=\"highlight\">测试用例执行失败%s</div>
                <div class=\"normal\">测试用例执行跳过%s个</div>
                <div class=\"normal\">执行时长-%s</div>''' % (run_result['测试用例']['成功'], run_result['测试用例']['失败'], run_result['测试用例']['跳过'], run_result['执行时间']),
            "url" : self.serve_url,
            "btntxt":"详情"
        }
        return textcard

    def __sendmsg(self, textcard):
        try:
            access_token = self.__get_access_token()
            if access_token:
                send_url=self.send_message_url + access_token
                send_info={
                    "touser" : self.target_user,
                    "toparty": self.target_party,
                    "msgtype" : "textcard",
                    "agentid" : self.agent_id,
                    "textcard" : textcard
	        	}
                send_info_urlencode = json.dumps(send_info)
                response=requests.post(url=send_url, data=send_info_urlencode)
                rep_info=response.content
                logging.info("企业微信发送消息结束，返回信息为%s" % rep_info)
                response.close()
            else:
                logging.error('企业微信通知-没有获取到token')
        except Exception as e:
            logging.error("企业微信通知-发送失败，具体错误为\n%s" % str(e))