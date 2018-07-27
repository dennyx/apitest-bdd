"""
redis mq操作
预准备，为后续可能需要关注redis mq中的内容
"""

import redis

class RedisPubAndSub(object):

    def __init__(self):
        self.__conn = redis.Redis(host='',port=6379)
        self.channel = 'channel_name' 

    def publish(self,msg):
        self.__conn.publish(self.channel,msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub