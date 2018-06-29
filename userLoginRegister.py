import pymysql

class MysqlHelper:
    def __init__(self,host='localhost',port=3306,db='Users',user='root',passwd='123456',charset='utf8'):
        self.conn=pymysql.connect(host=host,port=port,db=db,user=user,passwd=passwd,charset=charset)

    def lod(self,username,upwd):
        sql = 'select uname from userinfos'
        cs1 = self.conn.cursor()
        cs1.execute(sql)
        data3 = cs1.fetchall()
        for i in data3:
            if username ==i:
                return False


    def regert(self,username,upwd):
        sql = 'insert into userinfos(username, upwd) values(%s,%s)'%(unmae,upwd)
        cs1 = self.conn.cursor()
        cs1.execute(sql)
        self.conn.commit()
        cs1.close()
        self.conn.close()
        return True
