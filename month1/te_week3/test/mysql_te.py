from month1.week3.class8.qqq import DB
db = DB(host='localhost', port=3306, user='root', password='123',database='stu',dict=True)

sql ="""
    create table if not exists fgouser(
    username varchar(30) not null,
    password varchar(20) not null,
    PRIMARY KEY (username)
    )engine=InnoDB DEFAULT charset=utf8
"""# 如果没有fgouser表创建fgouser表
db.common(sql)# 提交sql语句到数据库
while True:
    print("请输入当前需要做的具体操作1,登录  2,,注册")
    num = input('请输入具体操作编号:')
    if num.isdigit():# 判读是否输入为整数
        num = int(num)
        if num ==1:
            username = input("请输入登录用户名")
            password = input("请输入登录密码")
            sql = 'select password from fgouser where username=%s'
            # 查询密码是否正确
            result = db.select(sql, username)
            if len(result)==0:
                print("对不起,不存在该账户")
            else:pass
        elif num == 2:
            username = input("请输入登录用户名")
            password = input("请输入登录密码")
            sql = 'select count(username) from fgouser where username=%s'
            result = db.select(sql, username)
            if result[0]['count(username)'] == 0:
                sql = "insert into fgouser(username,password)VALUES (%s,%s)"
                result = db.insert(sql,[(username,password)])
                if result >0:
                    print("注册成功")
                else:
                    print("注册失败")
            else:
                print("用户名以存在")




    else:pass





