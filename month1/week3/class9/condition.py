import threading
import time, random

"""

Condition():threading内置的高级锁对象,内部默认封装的是
一个RLock对象
Condition内部封装的也是acquire和release操作,只不过
该操作内部也是通过RLock来间接完成上锁和解锁过程,
同时Condition内部封装了一个线程等待池,只要线程通过调用
wait()方法,此时线程会被自动丢到等待池中,直到另一个线程通过
notify()/notifyAll()来唤醒在等待池中的线程

Condition一般适用于两个线程互相协作完成的任务
注意notify(n)默认每次唤醒一个线程,当指定n值时,可以同时唤醒n个线程

"""
con = threading.Condition()
# 该变量存储随机变量,判定两人谁输,谁赢
result = 0
# 定义一个负责找到孩子啊
def seeker(name):
    con.acquire()
    print('已经蒙好眼了,你可以去藏了!')
    con.wait()
    for i in range(3):
        print("%s is seeker" % name)
        time.sleep(2)
    global result
    result = random.randint(0,1)
    if result == 0:
        print('找到你了,我赢了')
    else:
        print('出来吧,我输了')
    con.notify()
    con.release()

# 定义另外一个孩子隐藏的过程
def hidden(name):
    con.acquire()
    for i in range(3):
        print('%s is hidding' % name)
        time.sleep(2)
    print('我已经藏好了!!')
    con.notify()
    con.wait()
    global result
    if result == 0:
        print('我输了')
    else:
        print('我赢了')
    con.release()

# 创建线程一执行seeker操作
thread1 = threading.Thread(target=seeker,args=('熊大',))
# 创建线程二执行hidder操作
thread2 = threading.Thread(target=hidden,args=('熊二',))
thread1.start()
thread2.start()
