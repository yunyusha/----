# 定义一个函数,输出任意一个给定的数据
def outPut(num1):
    num1+=20
    print(num1)
num1 = 20
outPut(num1)
print(num1)
'''

上面的一段代码中两个x分别代表实际参数和形式参数,注意函数在
调用过程中的实际参数中的数据在传递给形式参数的过程是一个拷
贝的过程因此在函数内部对形式参数所作数据操作都不会影响实际
参数的数据

'''
jihe = {1, 2, 3}
jihe.add(4)
print(jihe)
def append(date):
    date.add(10)
    print(date)
append(jihe)
print(jihe)

# 定义一个字典,在字典中存储一个人的名字,同时定义一个函数
# 完成对人名的修改
name_1 = {'name': '李飞'}
def name(dict):
    dict['name'] =  '飞飞飞'
    print(dict)
name_2 = name(name_1)
print(name_1)


"""

引用数据类型,作为函数参数被传入到函数内部时
在函数内部所作的操作等价于直接对该数据本身做操作
常用的引用数据类型有:列表,字典,元组,集合,对象

函数作为函数参数传入到函数内部,此时传入函数内部的函数被称为回调函数

比如函数B作为函数A的参数传入到A内部,在A内部调用函数B,此时B函数称为回调函数

回调函数的作用:可以将一些不确定的操作交给使用者来实现,从而实现代码功能的扩充

"""
def get_max(num1,num2):
    or_max = True
    if num1 < num2:
        or_max = False
    return or_max

def sort_name(num1, num2, callback):
    if callback(num1, num2) is True:
        num1 = num1 ^ num2
        num2 = num1 ^ num2
        num1 = num1 ^ num2
    return num1,num2
m,n = sort_name(40,50,get_max)
print(m, n)

# 定义一个函数,完成对列表数据的遍历,并且对每一次遍历结果任意已处理
def caouo(list1):
    for q1 in range(len(list1)):
        list1[q1] = list1[q1]*2
    return list1

def bianli(list1,lala):
    lala(list1)
    return list1
li2 = [1,2,3,9 ]
m1=bianli(li2, caouo)
print(m1)

def map_list(list1, callback): # 做列表的遍历 callback任意处理列表
    list2 = list(list1)
    for i in range(len(list2)):
        item = list2[i]
        result = callback(item)
        if (isinstance(result, str) and len(result) == 0)or result is None:
            list2[i] = None
        else:
            list2[i] = result

    while None in list2:
        list2.remove(None)
    return list2


