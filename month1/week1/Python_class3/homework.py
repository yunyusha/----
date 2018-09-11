import random

# 第一题 定义一个列表输出所存储15个[10,30]之间的随机整数，并输出对应的列表数据
names = []
for i in range(15):
    names.append(random.randint(10, 30))
print(names)

# 第二题定义一个列表，存储15个[10,30]之间的随机整数，求该列表中的15个随机数的最大值
names2 = []
for i2 in range(15):
    names2.append(random.randint(10, 30))
names2.sort()
print(names2)
print(names2[14])

# 第三题 定义一个列表，存储10个[10,15]之间的随机整数，求所有随机数的和
sum_list = 0

names3 = []
for i3 in range(10):
    names3.append(random.randint(10, 30))
    sum_list = sum_list + names3[i3]
print(names3)
print("随机数的和是%d" % sum_list)

# 第四题 使用双层for循环输出9*9乘法表
for i4 in range(1, 10):
    for j in range(1, i4+1):
        m = str(i4)
        n = str(j)
        k = str(i4*j)

        print(n+"x"+m+"="+k, end=" ")
    print(" ")
# 第五题 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
num5 = [1, 2, 3, 4]


num_s = []

for i5 in range(len(num5)):
    num_5 = [1, 2, 3, 4]
    num_5.remove(num5[i5])
    for i_5 in range(len(num_5)):
        num__5 = [1, 2, 3, 4]
        num__5.remove(num_5[i_5])
        num__5.remove(num5[i5])
        for i__5 in range(len(num__5)):

            num_s.append([num5[i5], num_5[i_5], num__5[i__5]])
print(num_s)
for ii5 in range(len(num_s)):
    for ii_z in range(len(num_s[ii5])):
        ii_1 = str(num_s[ii5][ii_z])
        print(ii_1, end="")
    print("")
print("能组成%d个无重复三位数数字" % len(num_s))

# 第六题 输出所有的水仙花数？（水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。）
num = []
for ii6 in range(10):
    num.append(ii6)
# print(num)
num6 = num
num_6 = num
num__6 = num
# print(num_6)
result = []
for i6 in range(len(num6)):
    num_6 = num
    for i_6 in range(len(num_6)):
        num__6 = num
        for i__6 in range(len(num__6)):

            sum_6 = (num6[i6]**3)+(num_6[i_6]**3)+(num_6[i__6]**3)

            sum_sum = str(num6[i6])+str(num_6[i_6])+str(num_6[i__6])
            sum_int = int(sum_sum)
            if sum_6>=100 and sum_6<=999:
                # print(sum_6)
                if sum_6 == sum_int:
                    result.append(sum_6)

print("所有水仙花数为%s" % result)

# 第七题 控制台输入n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。从编号为1的人开始报数，
# 数到3的那个人出列；出列人的下一个人又从1开始报数，数到3的那个人又出列；依此规律重复下去，直到
# 圆桌周围的人全部出列，请依次输出对应的出列顺序

n7 = int(input("请输入人数"))
num7 = []
for i7 in range(1,n7+1):
    num7.append(i7)
print(num7)



