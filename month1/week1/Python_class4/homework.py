# 第一题 1、	企业发放的奖金根据利润提成。利润(I)低于或等于10万元
# 时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按
# 10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万
# 元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
# 超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？



money = float(input("请输入金额"))
bonus = 0
if money <= 100000:
    bonus = money*0.1
elif money > 100000 and money <= 200000:
    bonus = 100000*0.1+(money-100000)*0.075
elif money > 200000 and money < 400000:
    bonus = (money - 200000)*0.05+100000*0.175
elif money > 400000 and money <= 600000:
    bonus = (money-400000) * 0.03 + 100000 * 0.175 + 200000 * 0.05
elif money > 600000 and money <= 1000000:
    bonus = (money-600000) * 0.015 + 100000 * 0.175 + 200000 * 0.08
elif money > 1000000:
    bonus = (money-1000000)*0.01+100000*0.175+200000*0.08+400000*0.015
else:
    print("输入错误")
print(bonus)

# 输入某年某月某日，判断这一天是这一年的第几天
year = int(input("请输入一个年份"))
month = int(input("请输入月份"))
day = int(input("请输入日期"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            years = 1   # 1是闰年
        else:
            years = 2
    else:
        years = 1

else:
    years = 2
month31 = {1, 3, 5, 7, 8, 10, 12}
month30 = {4, 6, 9, 11}
my_set = {1}
for i in range(1, month):
    my_set.add(i)

in31 = month31 & my_set
in30 = month30 & my_set
sumday = 0
if month > 2 and years == 1:
    sumday = 29+len(in30)*30+len(in31)*31+day
elif month > 2 and years == 2:
    sumday = 28 + len(in30) * 30 + len(in31) * 31 + day
elif month == 2:
    sumday = day + len(in31) * 31
else:
    sumday = day
print(sumday)

# 三 输入三个整数x,y,z，请把这三个数由小到大输出。
x = int(input("请输入整数x"))
y = int(input("请输入整数y"))
z = int(input("请输入整数z"))
xiao = [x, y, z]
xiao.sort()
print(xiao)

# 四有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
i = 1
i1 = 1
# 获得两数的分子分母存入列表
fenmu = [1, 2]
while i <= 18:
    fenmu.append(fenmu[i]+fenmu[i-1])
    i += 1

fenzi = [2, 3]
while i1 <= 18:
    fenzi.append(fenzi[i1]+fenzi[i1-1])
    i1 += 1

print(fenzi)
print(fenmu)
print(len(fenmu))
x = 0
# 每步通分计算所得分数的分子分母存入
sumfz = []
sumfm = []

for i4 in range(19):
    # 辗转相除法求最大公约数
    # 两数相乘除以最大公约数获得最小公倍数
    max_num = max(fenmu[x], fenmu[x+1])
    min_num = min(fenmu[x], fenmu[x+1])
    while max_num % min_num != 0:
        temp = max_num % min_num
        max_num = min_num
        min_num = temp
        # 最大公约数
    min_bei = (fenmu[x]*fenmu[x+1])//min_num   # 计算最小公倍数
    fenzi[x] = (min_bei//fenmu[x]) * fenzi[x]  # 获取通分后的分子
    fenzi[x + 1] = (min_bei // fenmu[x + 1]) * fenzi[x + 1]   # 获取通分后的分子
    fenzi[x + 1] = fenzi[x] + fenzi[x + 1]   # 获取通分后的分子并相加计算分数
    fenmu[x + 1] = min_bei
    # 获取通分两数共用的分母
    sumfm.append(min_bei)   # 分母存入
    sumfz.append(fenzi[x + 1])   # 分子存入
    x += 1
print(sumfz)
print(sumfm)
print(len(sumfm))
print(sumfm[18])
max_nums = max(sumfm[18], sumfz[18])
min_nums = min(sumfm[18], sumfz[18])
while max_nums % min_nums != 0:
    temps = max_nums % min_nums
    max_nums = min_nums
    min_nums = temps
print(min_nums)
print(sumfz[18]//min_nums)
print(sumfm[18]//min_nums)
# 5、	一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
# 求它在第10次落地时，共经过多少米？第10次反弹多高？
heg = 100
luo1 = []   # 存储每一次下落的距离
heg1 = []   # 存储每一次弹起的距离
for i in range(10):
    luo = heg   # 下坠的距离
    heg = heg / 2  # 弹起的距离
    luo1.append(luo)
    heg1.append(heg)
print(luo1)
print(heg1)
sum1 = 0
sum2 = 0
for x in range(len(luo1)):
    sum1 += luo1[x]
for y in range(len(heg1)-1):
    sum2 += heg1[y]
print(sum1+sum2)

# 第六题 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一
# 个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
# 究竟有几个数相加由用户通过控制台输入
snum6 = int(input("请输入几个数相加"))
num6 = input("请输入相加的数字")
sum6 = 0
if  int(num6)<10 and int(num6)>0:
    for i6 in range(1,snum6+1):
        sum6 = sum6 + int(num6*i6)
    print(sum6)
else:
    print("输入错误")

# 第七题 一个数如果恰好等于它的因子之和，
# 这个数就称为"完数"。例如6=1＋2＋3.编程
# 找出1000以内的所有完数
list7 = []
for i7 in range(1,1001):
    list7.append(i7)
print(list7)
k_7 = []
sum_li = 0
for i7_1 in range(len(list7)): # 对1-1000进行遍历
    for k7 in range(1,list7[i7_1]):  # 对数字进行遍历
        if list7[i7_1] % k7 == 0 and list7[i7_1] != k7:  # 寻找因数,除去数字本身
            k_7.append(k7)  # 找到的因数存入列表
            sum_li = 0
        if k7 == list7[i7_1]-1:  # 判断是否到所求因数的数的最后一位
            for jisuan in range(len(k_7)):  # 因数列表的数相加
                sum_li = sum_li + k_7[jisuan]
            if sum_li == list7[i7_1]:
                print(sum_li)
                sum_li = 0
    k_7 = []

# 8、猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了
#  一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每
# 早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见
# 只剩下一个桃子了。求第一天共摘了多少。

geshu = []
x8 = 1
for i in range(9):
   x8 = (x8+1)*2
   geshu.append(x8)
print(geshu)

# 9、有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都
# 不死，问一年中每个月的兔子总数为多少？
tuzi = [0, 0]
for month9 in range(1, 13):
    for zhang in range(len(tuzi)):
        if tuzi[zhang]<3:
            tuzi[zhang]= tuzi[zhang]+1
    duishu = tuzi.count(3)
    for x in range(duishu):
        tuzi.append(0)
    print(len(tuzi))
# 2 2 4 4 6

# 10、判断101-200之间有多少个素数，并输出所有素数
list10 = []
for i10 in range(101, 201):
    list10.append(i10)
print(list10)
k_10 = []
sum_li = 0
z_10 = []
for i10_1 in range(len(list10)):   # 对1-1000进行遍历
    for k10 in range(1, list10[i10_1]):  # 对数字进行遍历
        if list10[i10_1] % k10 == 0 and list10[i10_1] != k10:  # 寻找因数,除去数字本身
            k_10.append(k10)  # 找到的因数存入列表
            sum_li = 0
        if k10 == list10[i10_1]-1:
            # 判断是否到所求因数的数的最后一位
            if len(k_10) == 1:
                z_10.append(list10[i10_1])
    k_10 = []
print(z_10)

# 11、	将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
k_11 = []
fenjie = int(input("请输入正整数"))
fenjie2 = fenjie
m11 = []
x11 = 0
while True:
    for k11 in range(1, fenjie):
        if fenjie % k11 == 0 and fenjie != k11:  # 寻找因数,除去数字本身
            k_11.append(k11)  # 找到的因数存入列表
        if k11 == fenjie - 1:  # 判断是否到所求因数的数的最后一位
            x11 = len(k_11)
    if x11 > 2:
        m11.append(k_11[1])
    elif x11 == 2:
        m11.append(k_11[1])
        m11.append(k_11[1])
        break
    else:
        m11.append(fenjie)
        break
    if k_11[1] == k_11[len(k_11)-1]:
        break
    fenjie = k_11[len(k_11)-1]
    k_11 = []
print(m11)
print("%d =" % fenjie2 , end=" ")
for wan in range(len(m11)):
    print("%d" % m11[wan], end=" ")
    if wan+1 < len(m11):
        print("*", end=" ")

