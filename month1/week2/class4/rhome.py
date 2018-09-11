# 递归函数完成十进制转换二进制
# list1 = []
def change(n, list1=[]):
    if n//2 == 0:
        list1.append(n)
        list1.reverse()
        return list1
    else:
        yu = n % 2
        list1.append(yu)
        return change(n//2, list1)

print(change(256))
