# 定义一个函数求两个数的最大值
# def max_num(num1, num2):
#     max_1 = max(num1, num2)
#     return max_1
# num_1 = int(input("输入值"))
# num_2 = int(input("输入值"))
# num_3 = int(input("输入值"))
# x = max_num(num_1, num_2)
# print(x)

# 定义一个函数求两个数字中最小的数,并返回给外界
# def min_num(num1, num2):
#     min_1 = min(num1, num2)
#     return min_1
# x1 = min_num(num_1, num_2)
# print(x1)

# # 定义函数求三个数最大的
#
# def max_num20(*num20):
#     max20 = max(num20)
#     return max20
# ll = max_num20(1,2,3,4,5,6,111,111111,1584654,111564161,1321231)
# print(ll)
# 定义一个函数求两个数的最大公约数
# num_1 = int(input("请输入"))
# num_2 = int(input("请输入"))
# def gongyue(num1,num2):
#     max_num = max(num1, num2)
#     min_num = min(num1, num2)
#     while max_num % min_num != 0:
#         temp = max_num % min_num
#         max_num = min_num
#         min_num = temp
#     return min_num
# ff = gongyue(num_1,num_2)
# print(ff)
# 定义函数判断某一年份是否是闰年,如果是则返回True如果不是则返回False
# years = int(input("请输入"))
# def nian(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 x = True
#             else:
#                 x = False
#         else:
#             x = True
#     else:
#         x = False
#     return x
# aaa = nian(years)
# print(aaa)
