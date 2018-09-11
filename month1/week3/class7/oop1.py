"""
面向对象(OOP):以事物为中心,首先考虑完成本件事情需要哪些事物参与,然后考虑每一个具有的
行为和特征,最后由这些事物的具体实例通过执行自身功能完成本次事件

面向对象的特征: 封装,继承,多态
面向对象的核心是类和对象

类: 具有相同行为和特征的一类事物的抽象
对象: 由类具体化的实例,世间万物皆对象,注意面向对象中真正执行操作的是对象

"""

class Person:
    kind = '黄种人'

    """
    
    __init__:初始化方法:Python内置方法,在类中定义,当通过类创建具体实例时,该方法被系统自动调用

    self:指代类所创建的具体实例对象

    """
    def __init__(self, name, age, sex):
        """

        如果想要限制外界访问对象属性,此时在定义属性
        前面添加两个"__" ,此时该属性的访问权限只能在当前类中访问

        前后均加"__"为系统内部使用,尽量避免使用


        @property:直接修饰对应属性的getter方法,被修饰的getter方法的名字
        对应属性名一致,此时装饰器@property会自动生成跟该getter方法一致的
        setter方法的装饰器,该装饰器直接修饰与属性名一致的setter方法

        """
        self.__name = name
        self.__age = age
        self.__sex = sex
    # 普通方法,该方法未来被某一个Python具体的实例对象调用,self指代该实例对象
    def introduce(self):
        print("我叫%s,今年%d岁,性别%s" % (self.__name, self.__age, self.__sex))

    def study(self):
        print("%s正在学习" % self.__name)

    # getter方法:用来间接获取对应私有属性的值
    @property
    def sex(self):
        return self.__sex
    # setter方法,用来间接完成对私有属性值的修改
    """
    setter和getter方法的作用:可以灵活的设置对象私有属性的访问权限
    避免用户随意修改属性中的数据,可以有效保护数据的安全
    
    """
    @sex.setter
    def sex(self, sex):
        if sex == '男' or sex == '女':
            self.__sex = sex
        else:
            raise ValueError
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age >=0 and age<=120 and isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    @classmethod
    def eat(cls):
        print('正在吃饭的人品种属于%s' % (cls.kind))



# Person创建实例对象
# 对象属性的访问, 通过对象.属性来进行访问
per = Person("冰哥",20,'女')
per.sex = '男'
print(per.sex)
# per.age(40)
# per.sex = '男'
# print(per.__name)
# per1 = Person("永哥",33,'男')
# print(per.sex)
# 冰哥做自我介绍(对象的方法也是通过对象.属性访问)
per.introduce()
per.study()
per.age = 10
print(per.age)

"""

类属性: 直接在类中定义的属性称为类属性,比如kind,
类属性的所用权归当前类所有,对象只能够获取该属性,
但是不能修改该属性值

类方法:通过@classmethod修饰的方法属于类方法,该方法的所有权
属于当前类,对象只能调用不能修改
注意:类属性和类方法对应的计算机内存空间只有一个,所有属性
访问操作是操作的是同一块空间数据,这样做可以有效帮助我们减少
计算机内存开销

"""
per1 = Person('朱哥', 23, '男')
# Person.kind = '黑种人'
per2 = Person('松哥',21, '待定')
per1.eat()

