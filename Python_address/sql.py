import MySQLdb
import importlib
import sys
importlib.reload(sys)


class Mysqldb(object):
    def __init__(self):
        try:
            # 连接数据库
            self.conn = MySQLdb.connect(
                host="localhost",   # 主机地址
                user="root",    # 账号
                passwd="123456",
                port=3306,
                db="goodsview",   # 数据库名
                charset="utf8",
                use_unicode=True
            )
            # 游标对象
            self.cursor = self.conn.cursor()
        except Mysqldb.Error as e:
            print("创建数据库连接失败|Mysql Error %d: %s" % (e.args[0], e.args[1]))
            self.conn.close()

    # 销毁对象
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    # 查询数据库
    def query(self, sql):
        self.cursor.execute(sql)    # 执行sql语句
        data = self.cursor.fetchall()
        if data:
            return data
        else:
            return 0

    # 单条数据处理提交
    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()      # 向数据库提交
            return True
        except Mysqldb.Error as e:
            self.conn.rollback()    # 发生错误时回滚
            return False

    # 多条数据处理提交
    def executemany(self, sql, d_list):
        try:
            self.cursor.executemany(sql, d_list)
            self.conn.commit()
        except Mysqldb.Error as e:
            self.conn.rollback()


# 生成实例
myOperationdb = Mysqldb()
