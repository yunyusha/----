# ll = "静夜思"
# ll = ll.encode()
# # decode,将此盘中读取的数据按照utf-8进行解码显示数据
# print(ll.decode())
# # 字符串的身份识别
# name = "xiaocaicai123"
# print(name.isalnum())
# # 判断字符串是否只有字母或数字组成
# print(name.isalpha())  # 判断字符串是否只有字母组成
# print(name.isdigit())  # 判断字符串是否只有数字组成
#
# # 字符串替换
# name = '中国共产党万岁'
# print(name.replace("共产党", "*"*3))
# str.capitalize() 将首字母进行大写操作
#  str.lower()将全部大写换成小写
# str.title()每个单词首字母大写,其他全部小写
a = str.capitalize('dfhdh')

b = str.lower("SFDJDHD")

c = "dd12啊3dd ddd"
c.title()
c = c.encode()
c = c.decode()
print(c)
