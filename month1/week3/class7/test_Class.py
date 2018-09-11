
# 定义一个分数类:分别完成分数的加减乘除
"""

类如果没有继承object 为新式类
如果继承object 为经典类
开发中一般使用经典类

"""

class Fenshu(object):
    def __init__(self, fenzi=0, fenmu=1):
        self.__fenzi = fenzi

        if fenmu==0:
            raise ValueError('分母不为零')
        else:
            self.__fenmu = fenmu
    @property
    def fenzi(self):
        return self.__fenzi
    @fenzi.setter
    def fenzi(self,fenzi):
        self.__fenzi = fenzi
    @property
    def fenmu(self):
        return self.__fenmu
    @fenmu.setter
    def fenmu(self,fenmu):
        self.__fenmu = fenmu
    # 将分子分母转换成分子形式
    def zhuanhuan(self):
        min_value = min(self.__fenmu,self.__fenzi)
        max_value = max(self.__fenmu,self.__fenzi)
        while max_value % min_value !=0:
            temp = max_value % min_value
            max_value = min_value
            min_value = temp
        self.__fenzi//=min_value
        self.__fenmu//=min_value
        print("%s/%s" % (self.__fenzi, self.__fenmu))
        return 0
# 进行分数的计算

class jisuan(object):
    # 计算两个分数的和差积商
    def adjust(self, fc1, fc2, sign='+'):
        sign = sign.strip()
        if sign == "+":
            fz = fc1.fenzi * fc2.fenmu + fc2.fenzi * fc1.fenmu
            fm = fc1.fenmu * fc2.fenmu
            return Fenshu(fz, fm).zhuanhuan()
        elif sign == "*":
            fz = fc1.fenzi * fc2.fenzi
            fm = fc1.fenmu * fc2.fenmu
            return Fenshu(fz, fm).zhuanhuan()