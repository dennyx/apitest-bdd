'''
Redis连接客户端
'''

from ..DBBase import DbBASE
import redis
import logging

class RedisClient(DbBASE):

    def __init__(self):
        # TODO 增加数据库连接池
        self.init_base_info('REDIS')
        self.DEFAULT_CHECK_KEY = 'automation'

    def connect_db(self):
        """
        连接数据库
        """
        logging.info("Redis准备建立数据库连接，参数信息为 host-%s, port-%d, password-%s, dbname-%s" % (self.host, self.port, self.password, self.dbname))
        self.conn = redis.Redis(host=self.host, port=self.port, password=self.password, db=self.dbname)
        logging.info("Redis建立数据库连接成功，参数信息为 host-%s, port-%d, password-%s, dbname-%s" % (self.host, self.port, self.password, self.dbname))

    def check_db(self):
        '''
        检查数据库
        '''
        logging.info("Redis准备检查数据库连接，对应key为-%s" % self.DEFAULT_CHECK_KEY)
        result = self.get_value_by_key('automation')
        if not result:
            logging.error("Redis数据库连接校验失败，对应key为-%s" % self.DEFAULT_CHECK_KEY)
            raise Exception('Redis数据库连接校验失败')
        logging.info("DB2数据库连接校验成功，对应key为-%s" % self.DEFAULT_CHECK_KEY)

    def exe_sql(self, sql):
        """
        执行SQL
        """
        pass

    def close_db(self):
        """
        关闭连接
        TODO 需要查看接口来获取对应的方法
        """
        pass

    def add_set_value(self, key, value):
        """
        调整、增加某一个key的值
        """
        logging.info("Redis准备增加\修改key, key为%s, value为%s" % (key, value))
        result = self.conn.set(key, value)
        logging.info("Redis成功增加\修改key, key为%s, value为%s, 结果为%s" % (key, value, result))
        return result
    
    def get_value_by_key(self, key):
        """
        获取指定key的值
        """
        logging.info("Redis准备获取指定key的值, key为%s" % key)
        result = self.conn.get(key)
        logging.info("Redis成功获取指定key的值，key为%s, 值为%s" % (key, result))
        return result

