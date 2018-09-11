from month1.week3.class8.qqq import DB
db = DB(host='localhost', port=3306, user='root', password='123',    database='stu', dict=True)

# 创建表格
sql = """
    create table if not exists usersv(
    username varchar(30) not NULL ,
    password VARCHAR (20) NOT NULL ,
    PRIMARY KEY (username)
    )engine=InnoDB DEFAULT charset=utf8
"""
db.common(sql)

while True:
    print("请输入当前需要做的具体操作1:登陆,2:注册")
    num = input("请输入具体的操作编号")

    if num.isdigit():
        num = int(num)
        if num == 1:
            username = input("请输入用户名")
            password = input("请输入登录密码")

            sql ='select username from usersv where username = %s'
            # 执行查询操作
            result = db.select(sql, username)
            print(result)
        elif num == 2:
            username = input("请输入用户名")
            password = input("请输入登录密码")
            sql = "select count(username) from usersv where username=%s "
            result = db.select(sql, username)
            print(result)
            if result[0]['count(username)'] == 0:
                # 此时不存在该用户
                sql = "insert into users(username,password)values(%s,%s)"
                result = db.insert(sql, [(username, password)])
                print(result)
            else:
                print("该用户名已")
        else:
            print("暂无该指令")
    else:
        print("对不起本次输入的操作指令格式有误")

