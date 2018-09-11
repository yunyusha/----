# import :Python内置的导入模块的命令,可以用来将需要的资源
# 从指定的位置导入当前的Python文件
import random

"""

list列表,本质上是一个大容器,在该容器中存在若干个子容器
每一个容器都可以存储任意类型的数据,列表中元素的访问可以
通过list[index]访问,其中index代表子容器的下标,该下标从0
开始

"""
names = ["xian", "yikuai", "stn", "fff"]
# 获取列表数据
print(names[2])

# 列表中添加数据
names.append("ffffff")
# 列表中添加数据list.append(items);将数据item添加到列表
# 本次添加在列表最后添加

print(names)
# 插入 list.insert(index,obj):在指定的下表index处将元素obj添加到
# 列表中,该方法可以灵活决定元素添加的位置
names.insert(2, "ssss")
print(names)
# names.append()

# 获取列表的元素总数
conut = len(names)
print(conut)
# 列表的遍历
# 1.通过下表遍历
for i in range(conut):
    names[i] = i
print(names)
# 2.通过迭代直接获取列表元素
# for i in names:
#     print(i)

# 列表中元素的修改
# names[0] = 20
# print(names[0])

# 定义一个空列表,向该列表中存储10个20-30的随机整数
"""

random.random();生成0-1之间的随机数(小数)
random.randint(a,b):生成[a,b]之间的随机整数

"""
names1 = []
for i in range(10):
    names1.append(random.randint(20, 30))
# print(names1)
#
#
# # 列表排序  默认升序
# names1.sort()
# print(names1)
# names1.sort(reverse=True)
# print(names1)
print(names1)
print(names1.pop(3))
print(names1)
"""

排序 sort()对指定列表进行排序,默认排序方式是
从小到大排序,
reverse: 布尔类型,默认为False如果设置为True
则按照降序排序

"""


"""
删除 方式一 pop()默认从列表中最后一个元素返回给外界使用并删除
指定下标则从指定下标删除元素
print(names1.pop())

方式二 remove()移除列表中第一个与obj匹配的元素
names1.remove(20)

"""

