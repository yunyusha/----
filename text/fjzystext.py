# k_10 = []
# fenjie = int(input("请输入正整数"))
# fenjie2 = fenjie
# m = []
# x = 0
# while True:
#     for k10 in range(1, fenjie):
#         if fenjie % k10 == 0 and fenjie != k10:  # 寻找因数,除去数字本身
#             k_10.append(k10)  # 找到的因数存入列表
#             sum_li = 0
#         if k10 == fenjie - 1:  # 判断是否到所求因数的数的最后一位
#             x = len(k_10)
#     if x > 2:
#         m.append(k_10[1])
#     elif x == 2:
#         m.append(k_10[1])
#         m.append(k_10[1])
#         break
#     else:
#         m.append(fenjie)
#         break
#     if k_10[1] == k_10[len(k_10)-1]:
#         break
#     fenjie = k_10[len(k_10)-1]
#     k_10 = []
# print(m)
# print("%d =" % fenjie2 , end=" ")
# for wan in range(len(m)):
#     print("%d" % m[wan], end=" ")
#     if wan+1 < len(m):
#         print("*", end=" ")

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
print("%d =" % fenjie2, end=" ")
for wan in range(len(m11)):
    print("%d" % m11[wan], end=" ")
    if wan+1 < len(m11):
        print("*", end=" ")
