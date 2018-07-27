"""
数据库连接基类

"""

from .lib.abc import ABCMeta, abstractmethod
from config import BASE_CONFIG

class DbBASE(object):
    """
    检查数据库连接的基类
    """
    __metaclass__ = ABCMeta

    def init_base_info(self, dbType):
        self.host = BASE_CONFIG['DB']['INFO'][dbType]['HOST']
        self.port = BASE_CONFIG['DB']['INFO'][dbType]['PORT']
        self.username = BASE_CONFIG['DB']['INFO'][dbType]['USERNAME']
        self.password = BASE_CONFIG['DB']['INFO'][dbType]['PASSWORD']
        self.dbname = BASE_CONFIG['DB']['INFO'][dbType]['DB_NAME']

    @abstractmethod
    def connect_db(self):
        """
        连接数据库
        """
        pass

    @abstractmethod
    def check_db(self):
        '''
        检查数据库
        '''
        pass

    @abstractmethod
    def exe_sql(self, sql):
        """
        执行SQL
        """
        pass

    @abstractmethod
    def close_db(self):
        """
        关闭游标和连接
        """
        pass
