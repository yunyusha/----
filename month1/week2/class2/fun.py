import random
"""

函数:完成特定功能的代码段
函数分为定义和调用两部分,函数定义过程,函数内部的代码不会执行,
只有通过函数调用,函数内部代码才会执行
函数定义的语法:
def 函数名(参数列表)
    函数体

"""

def outPut():
    print("Hello World")

# 函数调用
m = outPut()


"""

函数的分类:
1.无参数无返回值的函数比如ouPut()函数
2.有参数无返回值random_int
3.无参数有返回值的函数如max_num()函数
4.有参数有返回值random_color(min,max)
函数参数分为:实际参数和形式参数

形式参数:函数定义过程中所传递的参数称为形式参数,
注意形式参数没有实际意义,只有当实际参数的值传递
给形式参数是,形参会被当成临时容器,存储该数据,
保函数执行过程中数据的使用

实际参数:函数调用过程中传递的参数称为实际参数,实际参数决定了
形式参数的数据类型和具体数据值

return: 函数调用结束的标志,作用是将return后面的内容返回给外界,
同时结束本次函数的调用,如果return后面有代码此时也不再执行,
因此函数调用过程中,函数代码必须放在return关键字的前面
"""
def max_num(num1,num2):
    print(max(num1, num2))
max_num(20, 30)

# 定义函数完成[0,1]的随机整数的返回
def random_int():
    return random.randint(0, 1)
num = random_int()
print(num)

# 定义一个函数,返回一个指定数据范围的随机颜色值
def random_color(min, max):
    if min > max:
        raise ValueError('min must be smaller than max')
    else:
        return (random.randint(min, max),random.randint(min,max),random.randint(min,max))

red, green, blue = random_color(0,255)
print(red, green, blue)

