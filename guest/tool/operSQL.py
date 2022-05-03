#coding=uft-8
from pymysql import cursors,connect

class operSQL:
    '''批量添加数据;查询数据  针对 mysql 操作'''
    def __init__(self):
        self.conn =connect(host='127.0.0.1',
                           user='root',
                           passwd='123456',
                           db='guest',
                           charset='utf8mb4',
                           cursorclass=cursors.DictCursor)
    def mul_insert(self,filename):
        with open(filename,'r') as f:
            if f is not None:
                for line in f:
                    li = line.split(',')
                    try:
                        with self.conn.cursor() as cursor:
                            sql = 'INSERT INTO sign_gust (realname,phone,email,sign,event_id,creat_time)
                                   VALUES  #未完
                            cursor.execute(sql)
                        self.conn.commit()
    def conn_close(self):
        self.conn.close()
    def phone_selct(self,phone):
        with self.conn.cursor() as cursor:
            sql = 'select * from sign_guest where phone=%s'
            cursor.execute(sql,(str(phone),))
            result = cursor.fetchone()
            print(result)

if __name__ == '__main__':
    op = operSQL()
    filename = ''
    op.mul_insert(filename)
    op.conn_close()

    op1 = operSQL()
    phone = ''
    op1.phone_select(phone)
    op1.conn_close()

