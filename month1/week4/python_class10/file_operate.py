# 打开文件

"""
mode:打开的方式

r,r+:以只读或读写形式打开,如果指定文件不存在,此时程序报错
如果指定文件存在,此时打开文件光标在文件内容的开头位置
(如果使用r+内容的写入,此时执行的是内容替换旧内容)

w,w+(以只写或者读写形式打开,如果指定文件不存在会自动创建该文件)
如果使用只写或读写方式打开,文件中之前的内容会被清空,此时相当于执
行的是文件内容的替换操作

wb,wb+ :作用和w,w+是一样大的,只不过打开文件时以二进制文件格式打开
rb,rb+ :作用和r,r+是一样大的,只不过打开文件时以二进制文件格式打开
综上,对于二进制文件,一般操作的是图片,音频,视频或压缩包数据
a,a+:以只写或读写方式打开文件,不过每一次打开光标会在文件的最后
此时,新内容会被直接放在原内容后面进行追加
ab+和a+作用相同,只不过打开的文件是以二进制格式打开
注意,如果使用a,a+,ab+打开文件时,如果文件不存在,此时计算机会:
自动创建该文件
"""

# file =open('./aa.txt', mode='r+', encoding='utf8')
# file.write('deefasedfdvxxrfnhssdgxsg')
# # str = file.read()
# print(str)

# 读取图片数据
file = open('./kkk.jpg', 'rb')
data = file.read()
file.close()
# file = open('./血.png','rb')
# data1 = file.read()
# file.close()
#
# file1 = open('./4.jpg','wb')
# file1.write(data)
# file.close()

# file1 = open('./4.jpg','wb')
# # data = file.readlines()
# file.close()
# # for item in data:
"""
tell():指明光标所在位置,seek(offset):人为移动光标的位置,
offset代表光标移动的偏移
"""
# file = open('./aa.txt','a',encoding='utf8')
# print(file.tell())
# file.write('576462286')
file = open('./aa.txt', 'r+', encoding='utf8')
str = file.read()
file.seek(0)
file.write('测试数据')
file.close()
