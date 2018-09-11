# 电脑类
class Computer:
    colling = "风扇"
    def __init__(self, price, system, size1, RAM, firm):
        self.__price = price
        self.__system = system
        self.__size1 = size1
        self.__RAM = RAM
        self.__firm = firm


    @property
    def RAM(self):
        return self.__RAM
    @RAM.setter
    def RAM(self, RAM):
        self.__RAM = RAM

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            raise ValueError

    @property
    def firm(self):
        return self.__firm

    @firm.setter
    def firm(self, firm):
        self.__firm = firm

    @property
    def size1(self):
        return self.__size1
    @size1.setter
    def size1(self, size1):
        self.size1 = size1


    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        self.__system = system
    @classmethod
    def play(cls):
        print("玩游戏电脑用%s" %cls.colling)
Computer.play()

t1 = Computer(3000,'ios','17','8','海尔')
t2 = Computer
print(t1.colling)
t1.colling = "水冷"
print(t1.colling)
t1.play()
t2.play()

# 电影类
class Movies:
    def __init__(self, country, language, actor, type, name):
        self.__country = country
        self.__language = language
        self.__actor = actor
        self.__type = type
        self.__name = name

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country):
        self.__country = country

    @property
    def language(self):
        return self.__language
    @language.setter
    def language(self, language):
        self.__language = language

    @property
    def actor(self):
        return self.__actor
    @actor.setter
    def actor(self, actor):
        self.__actor = actor

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name
