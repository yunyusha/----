# 分支结构
"""
if分支结构:适用于只有一种选择的时候

if 条件:
    代码操作

if-else:分支结构适用于两种选择情况

语法结构
if 条件:
    执行语句
else 条件:
    执行语句
注意:else是对if条件的否定,即当if条件不成立时执行

if-elif-elif-elif...else: 用于计算机需要从多余
两个条件的结果中做出选择

语法结构:
if 条件1:
    执行语句1
elif 条件2:
    执行语句2
elif...
else:
    执行语句n


"""
# num = int(input("输入一个整数"))
#
# if num & 1 == 0:
#     print("num为偶数")

# 定义一个变量存储一个数据,判断这数据是否在[3,6],如果在则输出该变量


"""

注意:在Pyhon中,通过代码之间的缩进来表示程序的层级关系,因此在代码书写时必须严格按照缩进执行

pass:Python内置关键字,代表空语句,一般用来充当程序的结构

"""

# 定义两个变量,分别存储两个整数,求两个整数的最大值
num1 = int(input("请输入一个整数"))
num2 = int(input("请输入另一个整数"))
# if num1 > num2:
#     print("最大数是num1=%d" % num1)
# else:
#     print("最大数是num2=%d" % num2)

# 通过控制台输入数字a和b,请输出a占b的百分比
if num2 > num1:
    num2 = num1 / num2*100
    print("百分比为%.2f%%" % num2)
else:
    raise ValueError("数字a输入的值必须比数字b输入的值小")
    # 抛出异常,可告知问题

# 定义三个变量,存储三个整数,求三个整数的中间值
num3 = int(input("请输入一个数"))
num4 = int(input("请输入一个数"))
num5 = int(input("请输入一个数"))

if num3 > num4:
    if num4 > num5:
        print("中间值是%d" % num4)
    else:
        if num3 > num5:
            print("中间值是%d" % num5)
        else:
            print("中间值是%d" % num3)
else:
    if num5 > num4:
        print("中间值是%d" % num4)
    else:
        if num3 > num5:
            print("中间值是%d" % num3)
        else:
            print("中间值是%d" % num5)
'''

max_num = max(num3, num4, num5)
min_num = min(num3, num4, num5)
middle = num3+num4+num5-max_num-min_num
print(middle)

在开发中,很多时候需要使用if-else的嵌套操作
max(num1,num2,num3...):求若干个数据中的最大值
min(num1,num2,num3...):求若干个数据中的最小值

'''
# 输入一个年份,输出该年份中,二月份的总天数
year = int(input("请输入一个年份"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("二月29天")
        else:
            print("二月28天")
    else:
        print("二月29天")
else:
    print("二月28天")

    # num1, num2, num3 = 10, 15, 20
    #
    # if num2 < num1 < num3 or num3 < num1 < num2:
    #     print("中间值是%d" % num1)
    # elif num1 < num2 < num3 or num3 < num2 < num1:
    #     print("中间值是%d" % num2)
    # else:
    #     print("中间值是%d" % num3)

    #输入一个月份判断该月份属于哪一个季节
