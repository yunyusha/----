# 用户通过控制塔输入一个数字,完成对应数目的"*"输出
# num1 = int(input("输入次数"))
# i = 1
# while i <= num1:
#     print("*", end=" ")
#     i += 1

"""

循环嵌套: 在for循环体中存在另一个for/while循环
构成嵌套关系的现象开发中常用双层for循环.

"""
#
# numh = int(input("输入次数"))
# numl = int(input("输入次数"))
#
# for k in range(numl):
#     for i in range(numh):
#         print("*", end=" ")

num1 = int(input("输入行数"))
x = 1
#
# while i <= num2:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     i += 1
#     print("")
# for i in range(num2):
#     for b in range(num2, i, -1):
#         print("*", end=" ")
#     print("")
if num1 & 1 != 0:
    num2 = (num1+1)//2
    for i in range(num2):
        for j in range(num2-i-1):
            print(" ", end="")
        for p in range(i+1):
            print("*", end=" ")
        print("")

    for m in range(num2):
        print(" "*(m+1) + "* "*(num2-m-1))
