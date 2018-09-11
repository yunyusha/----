# 字符串的定义
name = "小CC"
name1 = "qq"
name3 = """aaaaaaaaaaaaaaa
            nnnnnnn
"""
print(name3, end="")
"""

字符串操作:

"""

# 获取字符串中字符的长度
name4 = "rewrite"
print(len(name4))

print(name4[4])
# 字符串可以看成是一个特别的字符列表,
# 可以用for-in直接遍历获取所用字符
for item in name4:
    print(item)

print(name4)
print(name4.count('e'))
# 统计给定的字符在字符串中重复出现的次数

# strip删除字符串中左右两端以给定内容开头的内容

name = "xiaocaicai--"
name = name.lstrip("x")
name = name.rstrip("-")
# 不对原字符串进行修改
print(name)
print(name.strip("i a"))


n1ame = "小呆呆"
# print(n1ame.ljust(20, '*'))  # 内容左对齐
# print(n1ame.zjust(20, '*'))  # 内容右对齐
print(n1ame.center(100, "-"))  # 内容居中对齐
# 如果给定的内容宽度,没有达到指定的部分,
# 此时空余的部分以人为指定的内容内部填充

name9 = 'xiao cai cai'
print(name9.capitalize())

# 字符串分割
# 字符串的分割 split(sep,maxsize):sep: 代表分割所依据的方式,
# maxsize代表分割的最大次数,默认是将所得内容进行分割

info = "http://www.baidu.com/avi.gif;http://www.baidu.com//av2.gif;http://www.baidu.com/avi3.gif;"
# print(info.partition(";"))  # 只分割一次
print(info.split(";",  maxsplit=2))

 # 字符串按照指定格式进行拼接
name = "ty".join(["aa", "bb", "cc", "dd"])
print(name)
# 字符串拼接
name = "aa"+"bb"
print(name)
dict = {"age" : "20", "name" : "小ccc", "sex": "男"}
# 格式化字符串
infor = "我叫{name},今年{age}岁,性别{sex},未婚".format(**dict)
print(infor)
# 字符串编码

ll = "静夜思"
# 按照utf-8编码,将文本数据转换成二进制数据,进行磁盘存储
ll = ll.encode()
# decode,将此盘中读取的数据按照utf-8进行解码显示数据
print(ll.decode())
# 字符串的身份识别
name = "xiaocaicai123"
print(name.isalnum())
# 判断字符串是否只有字母或数字组成
print(name.isalpha())  # 判断字符串是否只有字母组成
print(name.isdigit())  # 判断字符串是否只有数字组成

# 字符串替换
name = '中国共产党万岁'
print(name.replace("共产党", "*"*3))

