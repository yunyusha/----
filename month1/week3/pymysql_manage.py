import pymysql
# 链接数据库
con = pymysql.connect(
    host = "127.0.0.1",
    port=3306,
    user = 'root',
    password="576462286",
    database="stu",
    charset = 'utf8'
)
# 创建表格
sql_creat = """
    create table if not EXISTS daociyiyou(
    sno VARCHAR (20) NOT NULL,
    name VARCHAR (20) NOT NULL,
    sex VARCHAR (10) NOT NULL,
    age INT,
    PRIMARY KEY (sno)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8
"""
# 生成游标对象pymysql.cursors.DictCursor:保证数据在查询之后以字典的形
# 式返回给外界,默认是以元组类型的数据返回
cursor = con.cursor(cursor=pymysql.cursors.DictCursor)

# # 执行sql语句
# result = cursor.execute(sql_creat)
# 执行数据的插入操作
sql_insert = """
    insert into student(sno,name,sex,age)VALUES (
    %s,%s,%s,%s)
"""
# result2 = cursor.executemany(sql_insert,[('11','二狗','男',20),('12','三毛','男',25),('13','狗蛋','男',35)])
# # 数据提交
# con.commit()

"""

服务器数据库数据的插入过程:
 1,链接数据额
 2,获取游标对象
 3, 定义插入语句
 4,执行excutemany()完成多条数据的插入
 5,执行数据commit()操作完成数据提交(最终执行表格数据存储)
 6,关闭数据库
"""



"""
获取查询结果:
cursor.fetchall():从查询结果中返回所有的查询内容
cursor.fetchmany(size):从结果中获取指定size的数据个数
fetchone():从查询结果中获取第一条数据

"""
# 删除
sql_delete = "delete from student where sno=%s"
result4 = cursor.execute(sql_delete,'11')
print(result4)


# 完成数据的查询
sql_select = "select * from student"
result3 = cursor.execute(sql_select)
print(cursor.fetchall())


# 数据的更新
sql_update = "update student set name=%s,sex=%s where sno=%s"
result5 = cursor.execute(sql_update,args=('xx','xxx',12))

con.commit()
# 关闭数据库
con.close()