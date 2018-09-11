# year = int(input("请输入一个年份"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("二月29天")
#         else:
#             print("二月28天")
#     else:
#         print("二月29天")
# else:
#     print("二月28天")


# num1, num2, num3 = 10, 15, 20

# if num2 < num1 < num3 or num3 < num1 < num2:
#     print("中间值是%d" % num1)
# elif num1 < num2 < num3 or num3 < num2 < num1:
#     print("中间值是%d" % num2)
# else:
#     print("中间值是%d" % num3)


# 输入一个月份判断该月份属于哪一个季节
month = int(input("请输入一个月份"))
if month <= 5 and month >= 3:
    print("春季")
elif month<=8 and month>=6:
    print("夏季")
elif month>= 9 and month<=11:
    print("秋季")
elif month == 1 or month == 2 or month == 12:
    print("冬季")
else:
    print("输入有误")
