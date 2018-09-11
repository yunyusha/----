# sorted 将列表排序处理
x = sorted([11, 20, -55, 111, 0])
print(x)
# sorted() 将列表经过key处理后排序再返回原值
y = sorted(x,key=abs)
print(y)

# 字符会转化成Ascll码大小进行比较
x_1 = sorted(['bbbb', 'asdd', 'Zsd','Csadd'])
print(x_1)

# key全转化为小写,进而忽略大小写
y_1 = sorted(x_1, key=str.lower)
print(y_1)

# 反向排序不必改动,传入第三个参数 revers-True
z_1 = sorted(x_1, key=str.lower, reverse=True)
print(z_1)
