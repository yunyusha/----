import re
# 正则表达式
'''

# 正则命令：
. :匹配任意字符(\n除外)
^:匹配字符串的开头
$:匹配字符串的结束字符
*:连续匹配0次或多次
+:连续匹配1次或多次
?:连续匹配0次或一次
{n}:连续匹配n次
{m:n}:连续匹配m~n次
[0-9a-zA-Z]:匹配一个字符,必须是数字0-9或字母a-zA-Z字符
[...],匹配来自字符集的任意字符
# [...x-y...]:匹配x~y范围的任意一个字符
[^0-9a-zA-Z]:匹配除了数字字母的任意一个字符,
但是该字符除0-9,a-z,A-Z以外的字符
():代表一个整体
\d:匹配一个数字字符//匹配一个十进制数
\w:匹配一个任何字母数字字符
\D:匹配一个非数字字符
\W:匹配一个非字母和数字的字符
\s:匹配任意一个空白符
\S:匹配任意一个非空白符
\b:匹配任意一个单词边界
\.:匹配一个字符"

'''

# 书写一个正则表达式判断一个数是否是小数或者小数
'^\d+\.?\d+*$'

# re模块关于正则表达式的操作
# 控制台接受一个手机号,使用re模块判定手机号是否合法,并输出判定结果
#
# name = input("请输入一个数字:")
# if re.match('^[1-9][0-9]{10}$', name) is not None:
#     print(re.match('^[1-9][0-9]{10}$', name).group())
# else:
#     print("傻B输错了!!")

'''

match:re    模块提供的方法,作用是匹配指定的字符串开头位置
是否和指定的正则表达式匹配,如果匹配则提取该内容,否则返回None
fullmatch:  re模块提供的方法,作用是匹配整个字符串是否和指定的的
正则表达式相吻合,如果吻合,则提取整个字符串,否则返回None
group():    直接从匹配内容中提取匹配的结果

search(regx, string): 直接从字符串中提取第一个满足正则表达式的结果数据

findall(regx,string): 直接从string中提取所有满足正则表达式结果的数据并以
一个列表的形式返回数据   

正则表达式符合贪婪原则:尽可能多的匹配更多的符合元素

finditer(regx,string):作用原理和findall相同,
但是返回结果不同的是该方法返回的是一个生成器

split(regx,string):将字符串string按照regx指定的正则表达式进行分割

'''
info2 = "小451212菜123"
# print(re.match('\d+', info2).group())

print(re.findall('[\u4e00-\u9fa5]+', info2))

itr = re.finditer('\d', info2)
print(next(itr).group())
print(next(itr).group())

con = 'Welcome to Lanou ZZP180701 class'
print(re.findall('\w+', con))

con1 = 'Welcome to Lanou, ZZP180701 class'
print(re.split(r'\W+', con1))

