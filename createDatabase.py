import pymysql

class MysqlCreate:
    def __init__(self,host='localhost',port=3306,db='Users',user='root',passwd='123456',charset='utf8'):
        self.conn=pymysql.connect(host=host,port=port,db=db,user=user,passwd=passwd,charset=charset)
    
    def rgert(self,username,upwd):
        sql = 'create database Users;'
        sql2 ='use Users;'
        sql1 = 'create table userinfos(id int primary key auto_increment,uname varchar(20),upwd char(40));'
        cs1 = self.conn.cursor()
        cs1.execute(sq0)
        cs1.execute(sql)
        cs1.execute(sq2)
        self.conn.commit()
        cs1.close()
        self.conn.close()