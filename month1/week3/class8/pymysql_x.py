import pymysql
class DB(object):
    def __init__(self,**kw):
        self.__conn = pymysql.connect(
            host = kw['host'],
            port = kw['port'],
            user = kw['user'],
            password = kw['password'],
            database = kw['database'],
            charset='utf8'
        )
        if kw['dict'] is True:
            # s生成游标对象,保证获取的数据是字典类型
            self.__cursor = self.__conn.cursor(pymysql.cursors.DictCursor)
        else:
            # 生成游标对象,获取的数据按元组类型返回
            self.__cursor = self.__conn.cursor()
    # 为DB添加数据插入操作
    def insert(self, sql, data):
        # 完成多条数据的插入操作
        result = self.__cursor.executemany(sql,data)
        # 将执行之后的结果提交给数据库最终完成数据库的修改
        self.__conn.commit()
        return result

    # 为DB添加数据查询操作
    def select(self,sql,data=()):
        # 执行查询操作
        self.__cursor.execute(sql, args=data)
        # 返回查询值后的数据
        return self.__cursor.fetchall()
    # 为DB添加数据删除功能
    def delete(self,sql,data):
        result = self.__cursor.execute(sql,args=data)
        self.__conn.commit()
        return result
    # 为DB添加数据更新功能
    def update(self,sql,data):
        result = self.__cursor.execute(sql,args=data)
        self.__conn.commit()
        return result
    # 添加通用操作
    def common(self, sql):
        result = self.__cursor.execute(sql)
        return result