import time
import functools
"""

闭包函数: 在函数A内部定义另外一个函数B,之后B作为A函数的返回值:
直接被返回,此时函数B称为A的闭包函数,在闭包函数B中如果使用了
A函数中定义的变量,此时A函数中被定义的变量会被临时存储,直到B函数
调用结束时该变量才会被系统回收,从而实现A中变量的延迟释放的时间

global:声明的变量属于全局变量,此时在使用该变量时,计算机直接到函数的最外层寻找是否
存在该变量
nonlocal: 声明的变量属于非本地变量,此时计算机不会在当前变量使用的函数寻找该变量
而是到该函数的外层寻找该函数比较近是对应变量进行应用

"""
# def put(num):
#     print(num)
#     def wrapper():
#         # global num
#         num = 10
#         num += 20
#         print(num)
#     return wrapper
# fun = put(11)
# fun()
# # num = 10
# # fun(5)

def put(num):
    print(num)
    def wrapper():
        nonlocal num
        num += 20
        print(num)
    return wrapper
fun = put(20)

fun()

# 双层装饰器
def log_time(fun1):
    @functools.wraps(fun1)
    def wrapp(*args, **kw):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return fun1(*args, **kw)

    return wrapp
@log_time # 等价于 now = log_time(now)
def now(*nu):
    print(nu)
print(now.__name__)
now(20, 30)
if now.__name__ is 'now':
    print('程序运行正常')
else:
    print('程序运行不正常')

# 定义一个带参数的装饰器
def log(txt):
    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kw):
            print(txt, end='')
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            return fun(*args, **kw)
        return wrapper
    return decorator

@log('你当前正在运行的函数对应的时间是:') # 等价于  max_num = log('你当前正在运行的函数对应的时间是:')(max_num)
def max_num(num1, num2):
    print(max(num1, num2))
max_num(10,20)
"""

装饰器:装饰器的作用是通过@语法,直接用定义好的函数修饰之前已经存在的函数,从而实现对原函数功能的扩充
1.不需要修改原代码,即可实现对原函数功能的扩充
2. 利于后期代码的维护

"""

