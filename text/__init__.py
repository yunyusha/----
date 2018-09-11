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
        if k7 ==list7[i7_1]-1:# 判断是否到所求因数的数的最后一位
            for jisuan in range(len(k_7)):  # 因数列表的数相加
                 sum_li = sum_li + k_7[jisuan]
            if sum_li == list7[i7_1]:
                print(sum_li)
                sum_li = 0
    k_7 = []
