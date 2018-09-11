import re
def cle_str(str_1): #
    x_1 = re.split(r'\W', str_1)
    q1 = ''
    for i1 in x_1:
        q1+=i1
    print(q1)
ze = cle_str('--sdg--as-')

def fi_num(str_2): # 完成字符串中数字的提取
    x_2 = re.findall(r'\d', str_2)
    print(x_2)
num = fi_num('sd14fsd41')


# 定义函数判断某一年份是否是闰年,如果是则返回True如果不是则返回False
# years = int(input("请输入"))
# def nian(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 x = '闰年'
#             else:
#                 x = '非闰年'
#         else:
#             x = '闰年'
#     else:
#         x = '非闰年'
#     return x
# aaa = nian(years)
# print(aaa)
sxh = []
def flow():  # 求水仙花数
    for i in range(100, 1000):
        q1 = i//100
        q2 = (i-100*q1)//10
        q3 = i-100*q1-10*q2
        if q1**3+q2**3+q3**3 == i:
            sxh.append(i)
m \
    = flow()
print(sxh)

erjin = []
def num_5(shijin):

    if shijin>=2:
        if shijin % 2 == 0:
            erjin.append('0')
            shijin = shijin//2
        else:
            erjin.append('1')
            shijin = shijin//2
        num_5(shijin)
    else:
        erjin.append('1')
        erjin.reverse()
        z_5 = ''
        for x_5 in erjin:
            z_5 += x_5
        print(z_5)
# s_5 = int(input("输入数字"))
m_5 = num_5(9)


def jiecheng(n): # 使用递归求数的阶乘
    m = 1
    if n>0:
        for i_6 in range(1, n+1):
            m = i_6 * m
    print(m)
x_6 = jiecheng(5)

def count_7(str_7): # 统计出其中英文字母、空格、数字和其它字符的个数
    enum = re.findall(r'[a-zA-Z]{1}', str_7)
    kong = re.findall(r'[ ]', str_7)
    shu = re.findall(r'\d', str_7)
    other = re.findall(r'[^\s\w]', str_7)
    print(enum)
    print(len(enum))
    print(kong)
    print(len(kong))
    print(shu)
    print(len(shu))
    print(other)
    print(len(other))
text = count_7('sddg onj 3  25\--asf1')

def Fs(geshu):
    fi = [0, 1]
    for f_8 in range(2, geshu):
        x = fi[f_8-2]+fi[f_8-1]
        fi.append(x)
    print(fi)
t_8 = Fs(5)


def yinzi(num_9): # 输出输入数字的所有因子
    yz = []
    for la in range(1, num_9):
        if num_9 % la == 0:
            yz.append(la)
    print(yz)
last = yinzi(100)

''''''