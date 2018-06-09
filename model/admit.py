from message.sql_helper import mysql_helper

class Admit():
    def __init__(self):
        self.__helper = mysql_helper()

    def Checkdata(self,username,password):
        sql = "select * From users where username = %s AND password=%s"
        params = (username,password)
        return self.__helper.getOne(sql,params)
