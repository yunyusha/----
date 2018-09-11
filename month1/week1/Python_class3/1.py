# list7 = []
# k_7 = []
# for i7 in range(1,1001):
#     list7.append(i7)
# print(list7)
# sum_li = 0
# for i7_1 in range(len(list7)): # 对1-1000进行遍历
#     for k7 in range(1, list7[i7_1]):# 对数字进行遍历
#
#         if list7[i7_1] % k7 == 0 and list7[i7_1]!=k7:# 寻找因数,除去数字本身
#             k_7.append(k7)# 找到的因数存入列表
#             sum_li = 0
#         if list7[i7_1] == k7-1:
#             for jisuan in range(len(k_7)):# 因数列表的数相加
#                 sum_li = sum_li + k_7[jisuan]
#             if sum_li == i7_1+1:
#                 print(sum_li)
#                 sum_li = 0
#     k_7 = []
# geshu = []
# x8 = 1
# for i in range(9):
#    x8 = (x8+1)*2
#    geshu.append(x8)
# print(geshu)

# tuzi = [0, 0]
# for month9 in range(1, 13):
#     for zhang in range(len(tuzi)):
#         if tuzi[zhang]<3:
#             tuzi[zhang]= tuzi[zhang]+1
#     duishu = tuzi.count(3)
#     for x in range(duishu):
#         tuzi.append(0)
#     print(len(tuzi))
# # 2 2 4 4 6

# list10 = []
# for i10 in range(101, 201):
#     list10.append(i10)
# print(list10)
# k_10 = []
# sum_li = 0
# z_10 =[]
# for i10_1 in range(len(list10)): # 对1-1000进行遍历
#     for k10 in range(1, list10[i10_1]):  # 对数字进行遍历
k_10 = []
k_102 = []
fenjie = int(input("请输入正整数"))
fenjie2 = fenjie

while True:
    for k10 in range(1, fenjie):
        if fenjie % k10 == 0 and fenjie != k10:  # 寻找因数,除去数字本身
            k_10.append(k10)  # 找到的因数存入列表
            sum_li = 0
        if k10 == fenjie - 1 :  # 判断是否到所求因数的数的最后一位
            print(k_10)
            x = len(k_10)
    if x == 3:
        fenjie = k_10[x // 2]
        kk = k_10
        break
    elif x == 2:
        fenjie = k_10[x // 2]
        q = k_10[1]
        k_10.append(q)
        kk = k_10
        break
    elif x == 1:
        k_10.append(fenjie)
        kk = k_10
        break
    else:
        fenjie = k_10[x// 2]
    k_10 = []

while True:
    for k102 in range(1, fenjie2):
        if fenjie2 % k102 == 0 and fenjie2 != k102:  # 寻找因数,除去数字本身
            k_102.append(k102)  # 找到的因数存入列表
            sum_li = 0
        if k102 == fenjie2 - 1:  # 判断是否到所求因数的数的最后一位
            print(k_102)
            x2 = len(k_102)
    if x2 == 3 :
        fenjie2 = k_102[(x2 + 1) // 2]
        kk2 = k_102
        break
    elif x2 == 2:
        fenjie2 = k_102[(x2+1) // 2]
        q2 = k_102[1]
        k_102.append(q2)
        kk2 = k_102
        break
    elif x2 == 1:
        k_102.append(fenjie2)
        kk2 = k_102
        break
    else:
        fenjie2 = k_102[(x2 + 1) // 2]
    k_102 = []
print("结果")
print(kk, kk2)
kk_1 = []
for las in range(len(kk)-1):
    las1 = str(kk[las+1])
    kk_1.append(las1)
for las_2 in range(len(kk2)-1):
    las2 = str(kk2[las_2+1])
    kk_1.append(las2)
print(kk_1)

