# x = 5
# s = sum(x*y for y in range(5))# 5+10+15+20
# q = x*sum(range(5))
# print(q)
# print(s)

def S(seq, i=0):
    if i == len(seq):
        return 0
    return S(seq, i+1) + seq[i]
x = [1, 2, 3, 4, 5, 6]
y = S(x)
print(y)

def T(seq,i=0): # 计算上面递归的次数
    if i == len(seq):
        return 1
    return T(seq, i+1) + 1
y = T(x)
print(y)
