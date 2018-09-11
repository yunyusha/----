import re
import random
def max_1(*mnum):
    num1 = max(mnum)
    return num1
x_1 = max_1(10,20,60)
print(x_1)

def min_1(*mnum_2):
    num2 = min(mnum_2)
    return num2
x_2 = min_1(10,20,60)
print(x_2)

def random_1(num_3,num_3_1):
    x = random.randint(num_3, num_3_1)
    return x
l_3 = random_1(100,200)
print(l_3)

def gys(num_4,num4_1): # 求最大公约数
    max_4 = max(num_4,num4_1)
    min_4 = min(num_4,num4_1)
    if max_4 % min_4 != 0:
        temp = max_4 % min_4
        max_4 = min_4
        min_4 = temp
    return min_4
x_4 = gys(100,500)
print(x_4)

sxh=[]
def flow():  # 求水仙花数
    for i in range(100, 1000):
        q1 = i//100
        q2 = (i-100*q1)//10
        q3 = i-100*q1-10*q2
        if q1**3+q2**3+q3**3 == i:
            sxh.append(i)
m=flow()
print(sxh)

def inf(**r): # 输出一个人员信息
    str = '姓名:{name},年龄{age},性别{sex}'
    print(str.format(**r))

xinxi = {'name':'hutai','age':18,'sex':'男'}
x_6 = inf(**xinxi)

def znum(str): # 提取任意一个字符串中所有的数字
    x = re.findall('\d+', str) # x =['196','12']
    l_7 = ""
    for i_7 in x:
        l_7=l_7+i_7

    print(l_7)
num_7 = znum('sdggddg1996sas5sf2')

def znum_2(str_1): # 将任意一个字符串的所有数字剔除
    x_8 = re.findall('\D+', str_1)
    l=""
    for i_8 in x_8:
       l=l+i_8
    print(l)
num_8 = znum_2('sdg654vv54sd42zc')

def zhong(str_9): # 定义一个函数提取任意一个字符串中所有的中文
    x_9 = re.findall(r'[\u4e00-\u9fa5]+', str_9)
    print(x_9)
zhongwen = zhong('sd说的sc5跟454你a')


