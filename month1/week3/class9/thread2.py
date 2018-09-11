from threading import Thread
import threading

"""
当多个线程出现修改同一个公共资源的时候,为了防止
多个线程同时争抢同一资源此时需要为一个线程对应的操作
执行上锁和解锁任务

"""

# 创建lock对象
# 该对象中内置两个方法,分别是acquire和release,其中
# acquire()是获取锁的过程(上锁),release是释放锁的过程
# (解锁).但是注意,如果程序运行过程中某一个线程调用
# acquire之后没有调用release解锁,此时就会出现死锁现象
# 此时会进入阻塞状态
lock = threading.Lock()
#　定义全局变量
count = 0
# 定义函数完成对公共资源的修改操作
def change(n):
    global count
    count += n
    count -= n

# 定义函数完成对count进行
# n次修改
def target1(n):
    # 获取锁,为当前线程上锁
    lock.acquire()
    for i in range(n):
        change(10)
    # 为当前线程释放锁
    # lock.release()
# 定义一个函数完成对count进行m次修改
def target2(m):
    lock.acquire()

    for i in range(m):
        change(8)
    lock.release()

# 创建两个子线程分别完成target1任务和target2任务
thread1 = Thread(target=target1,args=(10000000,),name='thread1')
thread2 = Thread(target=target2,args=(10000000,),name='thread2')

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(count)

