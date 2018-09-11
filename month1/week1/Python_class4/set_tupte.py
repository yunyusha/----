# 元组
tuple1 = (10, 20, 30)
print(tuple1[2])

w, h = (200, 300)
print(w, h)

# 元组遍历
for item in tuple1:
    print(item)
print(len(tuple1))

# 元组切片
print(tuple1[0:2]*3)

"""

元组中的元素是只读性质的,不允许用户修改

"""
# 集合(集合中的元素是无序的,同时集合中的元素不允许重复)

set1 = {1, 2, 3, 4, 5, 6, 0, 3, 3, "gert"}
set2 = {1, 2, 4, 5, 6, 8, 44, 22}
print(set1 & set2)
sss = set1 & set2
# & 求两个集合的交集,|求两个集合的并集 ^求两个集合的交集的补集

# 获取集合的元素个数
print(len(set1))

# 集合的遍历
for item in set1:
    print(item, end="")

# 成员运算符: in/not in 判断给定的元素是否在列表字典或元组集合中
# 身份运算符:is/ is not 判断给定的元素是否是某一个引用的数据

num1 = 1
# 判断指定的变量是否是某一种对应的数据类型
print(type(num1) is int)
print(isinstance(num1, int))
print(sss)
