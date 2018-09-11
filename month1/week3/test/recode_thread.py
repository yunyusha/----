# import threading
# from threading import Thread
#
# def sum_num(n):
#     # 获取当前执行该任务的线程对象
#     th = threading.currentThread()
#     print('当前正在执行的线程名字为%s' % th.name)
#     sum_re = 0
#     for i in range(n+1):
#         sum_re += n
#     print('求和结果%d' % sum_re)
#
# thread1 = Thread(target=sum_num, args=(100000000,),name='thread1')
#
# # 启动指定线程
# thread1.start()
#
# thread1.join(timeout=1)
# print('程序执行完毕')

# from threading import Thread
# import threading
#
# lock = threading.Lock()
# count = 0
# def change(n):
#     global count
#     count += n
#     count -= n
#
# def target1(n):
#     lock.acquire()
#     for i in range(n):
#         change(10)
#     # 为当前线程释放锁
#     lock.release()
# # 定义一个函数完成对count进行m此操作
#
# def target2(m):
#     lock.acquire()
#     for i in range(m):
#         change(8)
#     lock.release()
# thread1 = threading.Thread(target=target1, args=(1000000,),name='thread11')
# thread2 = threading.Thread(target=target2, args=(1000000,),name='thread22')
# thread1.start()
# thread2.start()
# print(threading.enumerate())
# thread1.join()
# thread2.join()
#
#
# print(count)
#

# import threading
# import time,random
# con = threading.Condition()
# def seeker(name):
#     con.acquire()
#     print('已经蒙好眼了,可以去藏了')
#     con.wait()
#     for i in range(3):
#         print("%s is seeker" % name)
#         time.sleep(2)
#     global result
#     result = random.randint(0, 1)
#     if result == 0:
#         print("找到你了,我赢了")
#     else:
#         print("出来吧,我输了")
#     con.notify()
#     con.release()
#
# def hidden(name):
#     con.acquire()
#     for i in range(3):
#         print('%s is hidding' % name)
#         time.sleep(2)
#     print('我已经藏好了!!')
#     con.notify()
#     con.wait()
#     global result
#     if result == 0 :
#         print('%s输了' % name)
#     else:
#         print("%s赢了" % name)
#
#     con.release()
#
# # 创建线程1执行seeker操作
# thread1 = threading.Thread(target=seeker,args=('aa',))
# thread2 = threading.Thread(target=hidden,args=('bb',))
# thread1.start()
# thread2.start()

# import threading,time
# sem = threading.BoundedSemaphore(5)
#
# def download():
#     print('当前执行下载任务的线程是%s' % threading.current_thread().name)
#     time.sleep(3)
#     sem.release()
#     sem.release()
#
# for i in range(50):
#     sem.acquire()
#     th = threading.Thread(target=download,name='thread{0}'.format(i+1))
#     th.start()

import random
import threading
import time
from threading import Event

# 创建Event对象
# 红绿灯管控操作
event = Event()

def light():
    count_r = 5
    count_g = 3
    count_y = 2
    # 纪律当前灯的状态(0红灯,1绿灯,2黄灯)
    state = 0
    while True:
        if state == 0:
            if event.isSet()==True:
                event.clear()
            time.sleep(1)
            count_r -=1
            if count_r == 0:
                print("红灯转绿灯")
                state=1
                count_r = 5
        else:
            if event.isSet()==False:
                event.set()
            time.sleep(1)
            count_g -=1
            if count_g == 0:
                print("绿灯转红灯")
                count_g = 3
                state = 0

# 定义函数完成汽车的运行
def car_run():
    while True:
        # 模拟一辆车通过的时间
        time.sleep(1)
        if event.isSet() == False:
            print('当前是红灯,所有车辆暂停运行')
            event.wait()
        else:
            print('当前有一辆汽车通过')

# 定义两个线程分别完成红绿灯的控制和汽车的控制
thread1 = threading.Thread(target=light,name='light')
thread2 = threading.Thread(target=car_run,name='car')
thread1.start()
thread2.start()