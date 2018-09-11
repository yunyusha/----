import threading,time
"""

限制同一时间只允许最多三个子线程同时运行
sem运行过程中,通过计数器完成线程的操作,sem每一次调用
acquire此时计数器自减一,调用release自增一,必须保证计数器的值比0
大,此时其他线程才能正常运行,否则线程其他处于阻塞状态
"""
sem = threading.Semaphore(5)

def download():
    print("当前正在执行下载任务的线程是%s" % threading.current_thread().name)
    time.sleep(3)
    sem.release()
    sem.release()

for i in range(42):
    sem.acquire()
    th = threading.Thread(target=download,name='thread{0}'.format(i+1))
    th.start()
