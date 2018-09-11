import random
"""

列表的创建

方式一:通过[]快速创建
方式二:通过list()方法创建,开发中通常用了进行其他数据向列表数据转换
方式三:通过表达式创建列表,语法结构|数学表达式 条件1 条件2 ...
数学表达式:用了产生一个数据
条件一:for循环用来执行数据的重复生成
其他条件可以使for循环也可以是if判断

方式四： 生成器，定义语法：
list1是一个生成器对象，该生成器可以根据开发者需要灵活决定数据
生成的数量，有效提高计算机内存的使用效率
如果需要生成一个数据，此时可以通过next(list1),保证生成器list1
对赌那出该数据,并且注意每一次使用next调用生成器推断数据是,生成
器都会在前一次推断的基础上推断下一个数据,如果推断过程超出生成器
负载范围,此时生成器会以异常StopIteration方式告知开发人员该推断
已经结束

另外生成器本质上也是可以进行迭代的迭代器,可以通过for-in遍历该迭代器,
取出所有的推断数据

"""
list1 = [1, 2, 3, 'aa', 'bb']

list2 = list(range(10))

list3 = [x**2 for x in range(1, 9) if x & 1 == 0]
print(list3)
# 使用表达式生成10个[5,10]的随机整数
list4 = [random.randint(5, 10) for i in range(10)]
# 第一句为列表所需表达式,之后为条件
print(list4)
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
list5 = (int(str(q)+str(q1)+str(q2)) for q in range(1, 5) for q1 in range(1, 5) for q2 in range(1, 5) if q != q1 and q != q2 and q2 != q1 if int(str(q)+str(q1)+str(q2)) > 100)
# print(list5)
# while True:
#     print(next(list5))
# # 输出水仙花数
# list6 = [int(str(q)+str(q1)+str(q2)) for q in range(10) for q1 in range(10) for q2 in range(10) if int(str(q)+str(q1)+str(q2)) > 100 and int(str(q)+str(q1)+str(q2)) < 999 if (q2**3)+(q1**3)+(q**3) == int(str(q)+str(q1)+str(q2))]
# print(list6)

"""

列表的数据提取
列表切片,通过指定切片范围,实现从原列表中提取一段数据的操作
注意:在切片过程中,切片得到的新列表,并返回给外界,原列表不会收到影响

切片的方式分为下面几种
第一中
list1[:]:获取整个列表数据
list[a:]:获取原列表中下标从a开始到结束的所用数据
list[:a]:获取原列表中从下标为0-a-1位置的所有数据
list[a:b]:获取原列表中从下标为a-b-1位置的所用数据

"""
list7 = [x for x in range(11)]
print(list7[10])

# 合并列表
lista = [1, 2, 3]
listb = [4, 5, 6]
listc = lista + listb
print(listc)

# 列表元素的复制 list*n 将list中,每一个元素重复n遍
print(lista*3)

# 列表反转
# list.reverse()直接将列表list中所用的内容反转
lista.reverse()
print(lista)

# list.count(obj)列表的统计 count(obj)统计obj早列表中出现的次数
liet = [1, 1, 1, 1, 1, 4, 4, 4, 5, 5, 9]
print(liet.count(1))

# 获取指定元素在列表中的位置(下标),只获取元素在列表中第一次出现的位置
print(liet.index(1))
print(liet.index(1))

# 判断某一个元素是否在列表中
print(1 in liet)
