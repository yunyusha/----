"""

 while 循环:
    格式:while循环条件:
            循环体

while 执行原理,首先程序会判读循环条件是否成立,如果成立
执行循环体,每当循环体执行完毕会自动跳转到条件判断,如果
条件判断成立,则继续执行下一次循环否则while循环结束

continue, 结束本次循环,当程序执行过程中遇到continue关
键字,则本次循环结束,程序直接跳转到条件判断

break:结束本层循环,当程序执行过程中遇到break,此时break
所在循环会被强制终止

辗转相除法求最大公约数

"""
# index = 1
# while index <= 100:
#     if index == 5:
#         index += 1
#         continue
#     print(index)
#     index += 1
# 一个整数加100是一个完全平方数,再加上168又是一个完全平方数,请问该整数是多少
#  2<=i<=84 2<=j<=84 i*j=168
#
# for i in range(2, 85, 2):
#     j = 168 / i
#     if i > j and j % 2 == 0:
#         n = (i-j)/2
#
#         x = n**2 - 100
#         if x > 0:
#             print(int(x))
i = 2
while i <= 84:
    i += 2
    j = 168 / i
    if i > j and j % 2 == 0:
        n = (i-j)/2

        x = n**2 - 100
        if x > 0:
            print(int(x))
# 辗转相除法求最大公约数
"""

首先判断两个数的最大值和最小值分别作为被除数和除数,
进行取余操作,如果余数为0,则最小值即为最大公约数,否
则此时将除数作为下一次 取余的被除数,本次的余数作为
下一次的除数,该过程不停重复,直到某一个取余结果为0,
此时除数中的数据即为最大公约数.

"""
num1 = int(input("请输入"))
num2 = int(input("请输入"))

max_num = max(num1, num2)
min_num = min(num1, num2)
while max_num % min_num != 0:
    temp = max_num % min_num
    max_num = min_num
    min_num = temp
print("数字的最大公约数是%d" % min_num)
