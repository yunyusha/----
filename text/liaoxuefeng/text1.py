# def add(x,y,abs):
#     return abs(x)+abs(y)
# print(add(-5,6,abs))
from functools import reduce

"""
map()函数接受两个参数,一个是函数,一个是Iterable,map将传入函数依次作用到
序列的每个元素,并把结果作为新的Iterator返回

"""
def f(x):
    return x**2
r = map(f,[1, 2, 3, 4, 5, 6, 7, 8])
print(next(r))
print(next(r))
m = list(r)
print(m)
"""
reduce 把一个函数作用在一个序列上,
reduce把结果继续和下一个元素做累计计算,
比如
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1,x2),x3),x4)

"""
# 序列求和
def add(x,y):
    return x+y

print(reduce(add,[1, 3, 5, 7, 9]))

# 列表变换成整数

def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))
"""
filter()函数用于过滤序列,filter()把传入的函数依次作用于
每个元素,然后根据返回值是True还是False决定保留还是丢弃该元素
filter()是一个实现筛选的函数
"""
# 把一个列表中删掉偶数只保留奇数
def is_odd(n):
    return n % 2 == 1
p = list(filter(is_odd,[1, 2, 3, 4, 6, 9, 10, 15]))
print(p)

# 把一个列表中的空字符串删掉
def not_empty(s):
    return s and s.strip()
p1 = list(filter(not_empty,['a', '' ,' B', None, 'C', ' ']))
print(p1)

# 定义一个生成器,并且是一个无限序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 定义一个生成器,不断返回下一个素数

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)
x = primes()
for m in range(5):
    print(next(x))