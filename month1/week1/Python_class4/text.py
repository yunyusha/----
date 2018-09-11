# # 输入某年某月某日，判断这一天是这一年的第几天
# year = int(input("请输入一个年份"))
# month = int(input("请输入月份"))
# day = int(input("请输入日期"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             years = 1 #1是闰年
#         else:
#             years = 2
#     else:
#         years = 1
# else:
#     years = 2
# month31 = {1, 3, 5, 7, 8, 10, 12}
# month30 = {4, 6, 9, 11}
# my_set = {1}
# for i in range(1, month):
#     my_set.add(i)
#
# in31 = month31 & my_set
# print(in31)
# in30 = month30 & my_set
# print(in30)
# sumday = 0
# if month>2 and years == 1:
#     sumday = 29+len(in30)*30+len(in31)*31+day
# elif month > 2 and years == 2:
#     sumday = 28 + len(in30) * 30 + len(in31) * 31 + day
# elif month ==2:
#     sumday = day + len(in31)*31
# else:
#     sumday = day
# print(sumday)
i = 1
i1 = 1
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
k = 1
sumfz = []
sumfm = []
for i4 in range(5):

    while True:
        if k % fenmu[x] ==0  and k % fenmu[x+1] == 0:
            break
        k += 1

    fenzi[x] = (k//fenmu[x])*fenzi[x]
    fenzi[x+1] = (k//fenmu[x+1])*fenzi[x+1]
    fenzi[x+1] = fenzi[x]+fenzi[x+1]
    fenmu[x+1] = k
    sumfm.append(k)
    sumfz.append(fenzi[x+1])
    x += 1

print(sumfz)
print(sumfm)
# 前五项正确,后面计算不出来