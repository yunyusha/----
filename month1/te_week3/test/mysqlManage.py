import pymysql
# 链接数据库
conn = pymysql.connect(
    host='localhost',
    port = 3306,
    user = "root",
    password = "123",
    database = "stu",
    charset = "utf8"
)

# 创建表格
sql_create = """
    create table if NOT EXISTS studenttest(
       sno varchar(20) NOT NULL,
            name VARCHAR(20) NOT NULL,
            sex VARCHAR(10) NOT NULL,
            age INT,
            PRIMARY KEY(sno)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8
"""
# 生成游标对象pymysql.cursors.DictCursor:保证数据查询之后以字典
# 形式返回给外界,默认是以元组类型的数据返回
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 执行sql语句
result = cursor.execute(sql_create)
# 执行数据的插入操作
sql_insert = """
    insert into studenttest(sno,name,sex,age)VALUES (%s,%s,%s,%s)

"""
# result = cursor.executemany(sql_insert,[('1','aa','bb',11)])
# 对于对数据进行修改的操作,均需要进行数据的提交(如下),而数据的查询不对数据进行改动
# ,不需要进行数据的提交
conn.commit()


