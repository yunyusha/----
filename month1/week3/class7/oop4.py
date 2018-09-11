from enum import Enum,unique
#  枚举类
"""
枚举类:定义一个类继承自Enum类,此时定义的类即为枚举类
枚举类可以帮助开发人员定义对应的常量,为每一个常量设置一个易于理解的名字,方便开发人员识别
@unique用来装饰枚举类,避免枚举类中出现值的重复
"""
@unique
class Week(Enum):
    Sunday = 7
    Monday = 1
    Tuesday = 2
    Wednesay = 3
    Thursday = 4
    Friday = 5
    Saturday = 6

# print(Week.Sunday)
def outPut(week):
    if week == Week.Sunday:
        print("今天周日")
    elif week == Week.Monday:
        print("今天周一")
    elif week == Week.Friday:
        print("今天周五")
    elif week ==Week.Wednesay:
        print("今天是周三")
    elif week ==Week.Thursday:
        print("今天是周四")
    elif week ==Week.Tuesday:
        print("今天是周二")
    else:
        print("今天周六")
# outPut(week=Week.Tuesday)