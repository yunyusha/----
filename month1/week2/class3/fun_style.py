"""

匿名函数: 函数名被隐藏
匿名函数定义语法
lambda 参数1,参数2,...:函数体
注意:匿名函数函数体只有一行代码,
并且该代码必须有运行结果
运行结果会被作为函数返回值自动返回
匿名函数没有函数名,因此通常是通过变量
接受该函数,之后通过变量名(参数列表)来
调用,同时匿名函数因为代码只有一句,
因此匿名函数值用来解决比较简单的数据计算问题

"""
#  匿名函数
# 第一种方案
# num = (lambda x:x**2)(10)
# print(num)

fun = lambda x: x**2

result = fun(12)
print(result)

# 定义一个匿名函数 返回任意两个数的大小比较
fun1 = lambda x, y:x > y
result = fun1(10,20)
print(result)

fun2 =lambda x1: x1 % 2 != 0
print(fun2(11))


# 定义一个递归函数完成n的阶乘操作
def factorial(n): # 使用递归求数的阶乘
    m = 1
    if n>0:
        for i_6 in range(1, n+1):
            m = i_6 * m
    print(m)
x_6 = factorial(3)

def jiecheng(n1):
    if n1 == 1:
        return 1
    else:
        return n1*jiecheng(n1-1)
result = jiecheng(12)
print(result)
# 定义一个函数完成1-100所有数字的和
def sum1(n2):
    if n2 == 0:
        return 0
    else:
        return n2+sum1(n2-1)
result2 = sum1(100)
print(result2)

# 定义一个递归,求1-n之间所有奇数的和
def sumj(n3):
    if n3 % 2 == 0 and n3>1:
        n4 = n3-1
        if n4 == 1:
            return 1
        else:
            return n4+sumj(n4-2)
    else:
        if n3==1:
            return 1
        elif n3 == 0:
            return "错误"
        else:
            return n3+sumj(n3-2)
result3 = sumj(44)
print(result3)

# 定义一个递归函数求1-n之间所有偶数的和

def sumo(n4):
    if n4 > 1:
        if n4 % 2 != 0:
            n4 = n4-1
            if n4 == 2:
                return 0
            else:
                return n4+sumo(n4-2)
        else:
            if n4 == 2:
                return 2
            elif n4 == 0:
                return "错误"
            else:
                return n4+sumo(n4-2)
    else:
        print("输入错误")
result4 = sumo(87)
print(result4)
"""

在函数定义的过程中,变量分为全局变量和局部变量:

全局变量:定义在函数外面的称为全局变量,全局变量的生命周期
从变量定义开始直到程序运行结束

局部变量:定义在函数内部的称为局部变量,局部变量的生命周期
只是在函数内部有效,当函数调用结束之后变量自动被系统回收

在Python程序中变量的使用遵循就近原则,如果想要在函数内部使用
全局变量,此时一定要使用glabal变量名,声明该变量是全局变量
注意:全局变量声明有风险,因此在开发过程中一般以局部变量为主,
只有在需要不同函数中访问同一个数据时才会使用全局变量

"""

