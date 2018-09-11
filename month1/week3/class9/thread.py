"""

进程: 一个正在执行的程序,称为一个进程
线程: 进程执行的最小单位,可以保证进程正常执行,一个进程中至少含有一个线程,
该线程称为主线程

"""
import threading

# 从threadiing模块中导入Thread类
from threading import Thread
# 获取主线程
# print(threading.main_thread())

def sum_num(n):
    # 获取当前执行该任务的线程对象
    th  = threading.current_thread()
    print("当前正在执行的线程名字为%s" % th.name)
    sum_re = 0
    for i in range(n+1):
        sum_re += i
    print(sum_re)

# 创建子线程
thread1 = Thread(target=sum_num, args=(10000000,),name='thread1')

# setDaemon(True):如果设置为True,则是将该线程设置为主线程守护线程,当主线程执行结束
# 的时候,该线程不管任务是否完成都会被系统强制终止
thread1.setDaemon(True)
# 启动指定的线程
thread1.start()

# join(timeout):设置主线程必须等待对应子线程执行,等待指定的时间time
# 之后,如果子线程没有结果返回,主线程不在等待仍然执行,如果时间之内结
# 果返回,主线程立刻执行,如果timeout设置为None(默认),此时主线程必须
# 等待子线程的结果才能返回
# thread1.join(timeout=None)


print("程序执行完毕")

# 获取当前正在运行的线程总数
print("正在运行的线程总数为%d" % threading.active_count())
# 输出当前运行的所有进程,并且以list格式返回00000000000
print(threading.enumerate())