"""
range()python内置操作，用来生成指定范围的一串连续数字
range()最终返回的是一个可以迭代的容器

range(num):此过程生成一个区间为[0,num)的一串连续数字
range(num1,num2):此操作生成从[num1,num2)的一串连续数字
range(num1,num2,num3):此操作生成[num1,num2)的间隔为num3
的一串数字

"""

nums = range(2, 10, 3)
# 生成从0-10的
print(list(nums))

"""

循环: 程序对某一段相同代码,连续不断地重复执行多次(两次以上)的操作

Python中的两种循环分为:
for循环和while循环,其中for循环也成为迭代

迭代: 从一个可迭代容器中,重复不停的取值过程.

for循环的语法结构
for variable in Iterator
    循环体
variable:变量,用来存储每一次迭代所取出的数据
Iterator:迭代对象用来存储数据的迭代容器
循环体:每一次迭代之后需要做的具体操作

"""


# 请输出1-100所有的偶数

# for i in range(2, 101, 2):
#     print(i)

# 请输出1-100所有数字的和
# sum1 = 0
# for i in range(1, 101):
#
#     sum1 = sum1 + i
# print(sum1)
#
# sum2 = 1
# for i in range(1, 101):
#
#     sum2 = sum2 * i
#     print(sum2)
# 输出1-100中第一个7的倍数
for i in range(1, 101):
    if i % 7 == 0:
        print(i)

else:
    print("for循环正常结束")
"""

break :强制结束break所在的循环,即使后面还有需要执行的循环,
该层循环也不再执行

for循环,while循环,可以和else绑定,else中的代码,会在循环正常结束之后执行(可用于调试)
如果循环在执行过程中被break意外中断,则else中的代码不会执行


"""
