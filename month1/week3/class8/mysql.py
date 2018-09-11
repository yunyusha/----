""""""
"""
mysql数据库中每一个数据库可以看成是一个文件夹,主要作用是用来存储
对应的表格(文件),如果我们需要存储数据,则数据需要存储在表格中数据可操作指令

show databases :显示mysql中所有数据库

create database stu :创建名为stu的数据库

drop databse stu : 删除名为stu的数据库

use stu 选择指定名字的数据库

表格操作的命令:
创建表格
create table infor(
    sno varchar(10) not null,
    name varchar(10) not null,
    sex varchar(10) not null,
    age int,
    major varchar(30) not null,
    classroom varchar(50) not null
)engine=innoDB default charset=utf8
向infor表格中插入数据
insert into infor(sno,name,sex,age,major,classroom)values(
'10','bb','cc',22,'dd','ee'),

select * from infor; 查询所有数据

select * from infor where age>=20;
select * from infor where age<=20 and age>=26;
从infor按照where设定的条件进行查询
查询年龄是否落在集合(20,30)中的数据
select * from infor where age in (20,30)

select * from infor order by age desc limit 0,2;
从infor表格中查询指定条件的数据,并且查询结束按照age降序排序,
排序之后从排序结果再获取两条数据,获取的起始位置下标为1

delete from infor where sno='10';
从表格infor中删除一条或多条数据

更新infor表格中的数据
update infor set age=25 where sno='10';

删除表格
drop table infor

like 模糊查询,查询结果中含有指定内容的数据,其中%代表任意字符,
_代表一个字符

select * from infor where name like '%小';

group by 按照指定字段进行分组查询,该查询操作需要和group comcat
()配合使用,group concat()将查询到的内容进行分组合并
select group concat(name),classroom from infor group by
classroom;

设置表格外键 foreign key(sno) reference infor(sno),当表格
设置外键之后,该表格的数据此时需要和关联表格的数据保持一致,避免出现数据内容不一致现象
score1
scorel
去除两个表中重复的内容
"""












