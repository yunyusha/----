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

sumfz = []# 分子
sumfm = []# 分母

for i4 in range(19):
    max_num = max(fenmu[x], fenmu[x+1])
    min_num = min(fenmu[x], fenmu[x+1])
    while max_num % min_num != 0:
        temp = max_num % min_num
        max_num = min_num
        min_num = temp #最大公约数
    min_bei = (fenmu[x]*fenmu[x+1])//min_num
    fenzi[x] = (min_bei//fenmu[x]) * fenzi[x]
    fenzi[x + 1] = (min_bei // fenmu[x + 1]) * fenzi[x + 1]
    fenzi[x + 1] = fenzi[x] + fenzi[x + 1]
    fenmu[x + 1] = min_bei
    sumfm.append(min_bei)
    sumfz.append(fenzi[x + 1])
    x += 1




print(sumfz)
print(sumfm)
print(len(sumfm))