import pymysql
import conf

class mysql_helper(object):
    def __init__(self):
        self.__conn_dict = conf.conn_dict #把数据库连接信息传入到conf中

    def getdict(self,sql,params):
        con = pymysql.connect(**self.__conn_dict) # **表示传入的是字典里的数据
        cur = con.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql,params)
        data = cur.fetchall()
        cur.close()
        con.close()
        return data

    def getOne(self,sql,params):
        con = pymysql.connect(**self.__conn_dict) #连接到数据库
        cur = con.cursor(cursor=pymysql.cursors.DictCursor)
        data = cur.fetchone()
        cur.close()
        con.close()
        return data
