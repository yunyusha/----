from month1.week3.class8.qqq import DB
MesMan=DB(
    host='localhost',
    port=3306,
    user='root',
    password='123',
    database='stu',
    dict=True
)
sql ="delete from users where username=%s"
MesMan.delete(sql,'12vv3')
