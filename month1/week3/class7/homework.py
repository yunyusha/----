# 车类
class Car():
    doing = 'move'
    def __init__(self, firm, price, seat, model, country):
        self.__firm = firm
        self.__price = price
        self.__seat = seat
        self.__model = model
        self.__country = country

    @property
    def firm(self):
        return self.__firm
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        if isinstance(price, int):
            self.__price = price
        else:
            raise ValueError
    @property
    def seat(self):
        return self.__seat
    @seat.setter
    def seat(self,seat):
        if isinstance(seat, int) and seat >= 2:
            self.__seat = seat
        else:
            raise ValueError
    @property
    def model(self):
        return self.__model

    @property
    def country(self):
        return self.__country

    @classmethod
    def move(cls):
        print(cls.move)

# 游戏类

class Game:
    pingtai = '电脑'
    def __init__(self, capacity, type, price, online, num):
        self.__capacity = capacity
        self.__price = price
        self.__type = type
        self.__online = online
        self.__num = num

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price>=0 and isinstance(price, int):
            self.__price = price
        else:
            raise ValueError

    @property
    def online(self):
        return self.__online

    @online.setter
    def online(self, online):
        self.__online = online

    @property
    def num(self):
        return self.__num
    @classmethod
    def play(cls):
        print("在%s下玩游戏" % cls.pingtai)

# 手机类
class Phone:
    color = '白'
    def __init__(self, price, firm, weight, size, system):
        self.__price = price
        self.__firm = firm
        self.__weight = weight
        self.__size = size
        self.__system = system
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        if price>0:
            self.__price = price
        else:
            raise ValueError
    @property
    def firm(self):
        return self.__firm
    @firm.setter
    def firm(self,firm):
        self.__firm = firm

    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self,weight):
        if weight>0:
            self.__weight = weight
        else:
            raise ValueError

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        self.__size = size
    @property
    def system(self):
        return self.__system
    @system.setter
    def system(self, system):
        self.__system = system
    @classmethod
    def call(cls):
        print("在打电话的是%s手机" % (cls.color))