'''
DB2连接客户端
Ref:
https://www.ibm.com/support/knowledgecenter/SSEPGG_9.5.0/com.ibm.db2.luw.apdv.python.doc/doc/c0054699.html
'''

from ..DBBase import DbBASE
import ibm_db
import logging
import json

class DB2Client(DbBASE):

    def __init__(self):
        # TODO 增加数据库连接池
        self.init_base_info('DB2')

    def connect_db(self):
        """
        连接数据库
        数据库连接字符串参考：DATABASE=JSSNX;HOSTNAME=192.168.191.3;PORT=50000;PROTOCOL=TCPIP;UID=jssnx;PWD=jssnx
        """
        conn_str = "DATABASE=%s;HOSTNAME=%s;PORT=%d;PROTOCOL=TCPIP;UID=%s;PWD=%s" % (self.dbname, self.host, self.port, self.username, self.password)
        logging.info("DB2准备建立连接，连接字符串为\n%s" % conn_str)
        self.conn = ibm_db.connect(conn_str, "", "")
        logging.info("DB2建立数据库连接成功，连接字符串为\n%s" % conn_str)

    def check_db(self):
        '''
        检查数据库
        '''
        check_sql = 'select 1 from dual;'
        logging.info("DB2准备对连接进行校验，校验sql为%s" % check_sql)
        check_result = self.exe_sql(check_sql)
        if not check_result:
            logging.error("DB2数据库连接校验失败， 校验sql为%s" % check_sql)
            raise Exception('DB2数据库连接校验失败')
        logging.info("DB2数据库连接校验成功，校验sql为%s" % check_sql)

    def exe_sql(self, sql):
        """
        执行SQL
        """
        logging.info("DB2准备执行sql, sql为%s" % sql)
        stmt = ibm_db.exec_immediate(self.conn, sql)
        origin_dic = ibm_db.fetch_assoc(stmt)
        result_dic = []
        while origin_dic != False:
            origin_dic = ibm_db.fetch_assoc(stmt)
            result_dic.append(origin_dic)
        logging.info("DB2执行sql成功，sql为%s, 结果为%s" % (sql, result_dic))
        return result_dic

    def close_db(self):
        """
        关闭游标和连接
        """
        logging.info("DB2准备关闭数据库连接")
        ibm_db.close(self.conn)
        logging.info("DB2关闭数据库连接成功")

if __name__ == '__main__':
    client = DB2Client()
    client.connect_db()
    result = client.exe_sql('select * from BK_CUST_360_BASICINFO;')
    print(result)