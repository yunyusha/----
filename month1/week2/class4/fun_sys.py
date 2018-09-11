import functools
# 获取绝对值
print(abs(-5))
# 列表遍历
def callback(num):
    num **= 2
    return num
x = map(callback,[1,2,3,4,5])
print(list(x))


result = map(lambda x: x**2, [1, 2, 3, 4, 56])
print(list(result))

"""

map(fun, list):map用来完成对列表list的遍历操作
每一次遍历都会自动调用fun函数完成对本次遍历
所得元素的计算,当遍历结束之后返回一个map对象.

"""

"""
列表过滤:
filter(fun, list):用来遍历列表list,按照给定的过滤条件,
完成对满足条件的数据的过滤操作,其中fun对应的是回调函数
,充当过滤条件,因此fan返回结果必须是布尔类型的结果,如果结果
为True此时保留该元素,如果为False删除对应元素。
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'sfssdvbb']

result = filter(lambda x: isinstance(x,str),list1)
z = list(result)
print(z)

"""

偏函数:
将指定的函数和函数中默认的参数进行绑定,生成一个新的函数
比如:把int函数和int的默认参数base绑定生成一个新函数int2,
int2此时进行数据转化时按照二进制数据进行转换

"""
# def int2(num, base=2):
#     return int(num, base=base)

int2 = functools.partial(int, base=2)
result = int2('1010101')
print(result)

