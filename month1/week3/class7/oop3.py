""""""
"""

多继承

"""
# 新式类
class Tool(object):
    def __init__(self, **kw):
        print('当前正在执行tool的初始化操作')
        self.__name = kw['name']
        self.__weight = kw['weight']
        self.__speed = kw['speed']
    @property
    def name(self):
        return self.__name


class Ship(Tool):
    def __init__(self, **kw):
        print('当前正在执行ship的初始化操作')
        super().__init__(**kw)
        self.__waterp = kw['waterp']
        self.__watere = kw['watere']
    def float_water(self):
        print("%s当前正在水上航行" % self.name)

class Plane(Tool):
    def __init__(self,**kw):
        print('当前正在执行plane的初始化操作')
        super().__init__(**kw)
        self.__flyH = kw['flyH']
        self.__company = kw['company']
    def fly_move(self):
        print("%s当前正在飞行" % self.name)
class WaterPlan(Plane, Ship):
    def __init__(self, **kw):
        print('当前正在执行waterplane的初始化操作')
        super(Plane,self).__init__(**kw)
        self.__gl = kw['gl']


# 创建水上飞机对象
wp = WaterPlan(name='小丸子', weight='150吨', speed='60公里', waterp='10米', watere='1000吨', flyH='50米', company='任天堂', gl='110')
# wp.float_water()
# wp.fly_move()
"""

多继承:子类可以同时拥有多个父类的现象,称为多继承
多继承的优点,子类可以通过多继承的操作,获得比较丰富的属性和功能
同时多继承可以将父类中的代码进行分解,方便进行代码的维护

super():python内置的函数,主要应用于继承操作 ,作用,首先获取
当前所在类的对象,其次调用该对象分别执行其父类对应的方法
super():在执行父级元素筛选的时候,遵循/MRO算法(深度优先算法),
在多继承中首先查找该类最左边的父类,其次在查找该父类的父类,直到
基类,其次在查找下一个父类,查找原则同上,直到找到所有父类,
注意:如果查找过程中有多个类重复,则以最后查找到的为准
"""
