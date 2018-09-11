import random
import threading
import time
from threading import Event
"""

Event:事件处理机制,全局定义了一个Flag,如果Flag值
为False,那么当线程执行event.wait(),此时该线程进入
阻塞状态,但是如果Flag为True,此时线程调用event.wait()
线程不会处于阻塞状态
clear : 设置Flag为False
set: 设置False为True
isSet():判定当前Flag是否是True,默认状态下Flag为False
Event可以实现线程间的通信,使用Event可以使某一个线程
处于等待(阻塞)状态,等待其他线程通过set方法将Flag设置
为True,此时所有等待状态线程都会被唤醒

"""
# 创建Event对象
# 红绿灯管控操作
event = Event()
# 创建一个红绿灯
def light():
    count_r = 5
    count_g = 5
    count_y = 3
    # 记录当前灯的状态(0红灯,1绿灯,2黄灯)
    state = 0
    while True:
        if state == 0:
            if event.isSet() == True:
                event.clear()
            time.sleep(1)
            count_r -=1
            if count_r == 0:
                print("红灯转成绿灯")
                state = 1
                count_r=10
        elif state == 1:
            if event.isSet() == False:
                event.set()
            time.sleep(1)
            count_g -=1
            if count_g == 0:
                print("绿灯转成黄灯")
                state =2
                count_g = 5
        else:
            time.sleep(1)
            count_y -= 1
            if count_y==0:
                print("黄灯转成红灯")
                state = 0
                count_y = 3

# 定义函数完成汽车的运行
def carrun():
    while True:
# 模拟一辆车通过的时间
        time.sleep(1)
        if event.isSet() == False:
            print("当前是红灯/或者是黄灯,所有车辆暂停运行")
            event.wait()
        else:
            print("当前有一辆汽车通过")

# 定义两个线程分别完成红绿灯的控制和汽车的控制
thread2 = threading.Thread(target=light, name='light')
thread1 = threading.Thread(target=carrun, name='car_run')
thread1.start()
thread2.start()








