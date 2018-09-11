"""

字典:通过若干个键值对存取数据,每一对键值对都包含两部分
:key,value,从字典中存取数据可以直接根据key实现,因此数
据根据存取效率比列表更加高效

"""

infor = {"name": "ddd", "sex": "男"}

# 字典的拼接  dic1.update(dic2):视同字典dic1对dic2做数据更新
# 如果dic2中对应的键值对对dic1之前不存在,此时对该键值对执行拼接操作,
# 如果该键值对中 键存在,此时执行数据更新
diel = {"name": "翠花", "sex": "女"}
diel2 = {"name": 30, "class": "计算机应用"}
diel.update(diel2)
print(diel)

# die.pop : 删除指定的键值对
# 统计字典中键值对的个数

print(diel.pop("class"))
print(diel)
# dic.get(key):根据指定的key来获取value
# 该方法可以保证数据获取的安全性,即当没有
# 对应的kye时,计算机会返回一个None类型的数据

# 字典数据的遍历
# for in直接遍历字典,得到的时字典的key
for key in diel:
    print(diel.get(key))

print(diel.items())
# for in 通过字典的items()方法遍历字典,此时得到的是对应的键值对
# 的key和值两部分内容
for key, value in diel.items():
    print(key+":"+str(value))
# 获取字典中所用的键
print(diel.keys())

# 获取字典中所有的值
print(diel.values())

# type :获取指定数据类型,经常用来进行数据类型的判别
print(type(dict) is diel)
