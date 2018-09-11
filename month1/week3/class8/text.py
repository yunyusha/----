from month1.week3.class8.qqq import DB
db = DB(host='localhost', port=3306, user='root', password='123', database='stu', dict=True)
sno=17
name =  'qq'
sex = 'nan'
age =15
sql = "insert into student(sno,name,sex,age)VALUES (%s,%s,%s,%s)"
db.insert(sql, [(sno, name, sex, age)])
