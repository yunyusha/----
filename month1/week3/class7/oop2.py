"""

"""
class Person:
    def __init__(self, **kw):
        self.__name = kw['name']
        self.__sex = kw['sex']
        self.__age = kw['age']
        self.__height = kw['height']
        self.__weight = kw['weight']
    @property
    def name(self):
        return self.__name
    @property
    def sex(self):
        return self.__sex
    @property
    def age(self):
        return self.__age
    @property
    def height(self):
        return self.__height
    @property
    def weight(self):
        return self.__weight
    def introduce(self):
        print('我叫%s,今年%d岁,性别%s,身高%d,体重%d' % (self.__name, self.__age, self.__sex, self.__height, self.__weight))

    def jiaotan(self):
        print('我们当前正在交谈')
"""
继承的语法格式
class 子类(父类)
    pass
定义一个子类,继承子类一个指定的父类,注意:子类在继承父类时,会将父类所有特征和行为全部继承

子类从父类继承的所有方法的处理操作包括 照搬 ,重写,添加
"""

class Student(Person):
    def __init__(self, **kw):
        Person.__init__(self, **kw)
        self.__sno = kw['sno']
        self.__classroom = kw['classroom']
        self.__major = kw['major']
        self.__school = kw['school']
    # 重写
    # def introduce(self):
    #     print('我叫%s,今年%d岁,性别%s,身高%d,体重%d ,就读于%s,学号是%s,专业是%s' % (self.name, self.age, self.sex, self.height, self.weight, self.__school,self.__sno,self.__major))
    # 添加(在原函数功能基础上重新添加一部分新的功能)
    def introduce(self):
        Person.introduce(self)
        print("我目前就读于%s,专业是%s,班级是%s班,学号%s" % (self.__school, self.__major, self.__classroom,self.__sno))

stu = Student(name='冰冰', sex='女', age=23, height=110, weight=45, sno='11221122', major='播音主持', classroom='播音02', school='中央戏剧学院')
# stu.introduce()
# ren = Person(name='冰冰', sex='女', age='23', height=160, weight=45)
stu.introduce()

"""

子类从父类所继承的所有行为存在三种操作:
1.照搬: 直接通过子类对象调用从父类继承的方法
2.重写: 重新定义从父类继承的方法的实现,此过程可以实现面向对象
的多态操作, 多态, 同一个方法,不同对象在调用时执行结果不同,此过程称为方法的多态
3.添加: 从父类继承的方法在调用时,先通过父类调用该方法,之后在添加子类具体操作

"""
