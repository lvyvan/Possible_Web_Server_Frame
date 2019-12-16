#_*_ coding:utf-8 _*_
import pymysql

class MysqlHelper(object):
    def __init__(self, hostPar='127.0.0.1',
        portPar=3306,
        userPar='root',
        passwordPar='123456',
        databasePar='stock_db',
        charset='utf8mb4'):

        self.conn = pymysql.connect(
            host = hostPar,
            port=portPar, user=userPar,
            password=passwordPar,
            database=databasePar,
            charset=charset)
        self.curs = self.conn.cursor()

    def __del__(self):
        self.curs.close()
        self.conn.close()

    def select(self, sql, params = []):
        count = self.curs.execute(sql, params)
        return (count, self.curs)

    def execute(self, sql, params = []):
        count = self.curs.execute(sql, params)
        self.conn.commit()
        return count
