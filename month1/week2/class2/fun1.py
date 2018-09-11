

# 必须参数:程序执行过程中,必须要设置的参数
# 默认参数:程序运行过程中,具有默认值的参数
# 区别: 默认参数和必须参数就是参数是否提前设置好默认值
# 默认参数在函数调用过程中可以默认省略
def outPut(num):
    print(num)
def outPut1(num1=0):
    print(num1)
# 定义函数求任意个数值的和

# 可变参数的语法结构:
# 在必须参数前面添加*,此时参数变成可变参数
# 作用,参数的多少,可以根据函数在调用过程中,实际参数的
# 数量灵活增长,可变参数的数据类型是一个元组类型
# 可变参数需要放在默认参数的后面
# 可变参数与关键字参数常用
def get_sum(*arguments):
    print(arguments)
    sum_num = 0
    for item in arguments:
        if isinstance(item, list):
            sum_num += sum(item)
        else:
            sum_num += item

    return sum_num
num = get_sum( 10, 15, 20,[1, 2, 3, 4, 5])
print(num)
# 关键字参数
def outPut_userInfor(**kw):
    print(kw)
    for key, value in kw.items():
        print(key, ":", value)
        # print(value)
infor = {'name':"小星星","age":20, 'sex':'男','score':70}
o = outPut_userInfor(**infor)

# 定义一个函数,利用关键字参数,输出一个学生的自我介绍信息
# 姓名,年龄,性别,婚姻状况,专业,班级和学校

def image(**st):

    str = "我叫{name},性别{sex},今年{age},{marry},来自{school}{class}班{major}专业"
    print(str.format(**st))
infor2 = {'name':"小星星","age":20, 'sex':'男','marry':'未婚',"school":"一中","class":14,"major":"计算机"}
o2 = image(**infor2)

'''

关键字参数: 在必须参数前面加**,此时参数变成关键字参数
外界在调用函数时,必须为每一个数据设置唯一的键,或者通过**dict的格式
直接将摸一个字典类型的数组作为该关键字的参数的数据输入

'''

'''

命名关键字参数:
在所有参数的最前面设置一个*,此时后面的所有参数都被看成是提前定义好
名字的参数,外界在调用该函数的时候,每一个参数名字都必须和后面参数的
名字保持一致

'''
def put(*,name,sex,age):
    print(name, age, sex)

put(name=20,sex=10,age=111)






