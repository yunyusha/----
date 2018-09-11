# import multiprocessing
# import time
# def worker(interval):
#     n = 5
#     while n>0:
#         print("The time is {0}".format(time.ctime()))
#         time.sleep(interval)
#         n -= 1
#
#
# p = multiprocessing.Process(target=worker, args=(3,))
# p.start()
# print("p.pid", p.pid)
# print("p.name", p.name)
# print("p.is_alive:", p.is_alive())
#
#
import multiprocessing
import time

# def worker(interval):
#     n = 5
#     while n > 0:
#         print("The time is {0}".format(time.ctime()))
#         time.sleep(interval)
#         n -= 1
#
# if __name__ == "__main__":
#     p = multiprocessing.Process(target = worker, args = (1,))
#     p.start()
#     print(p.pid)
#     print("p.name:", p.name)
#     print("p.is_alive:", p.is_alive())

# def worker_1(interval):
#     print("worker_1")
#     time.sleep(interval)
#     print("end_worker_1")
#
# def worker_2(interval):
#     print("worker_2")
#     time.sleep(interval)
#     print("end worker_2")
#
# def worker_3(interval):
#     print("worker_3")
#     time.sleep(interval)
#     print("end worker_3")
#
# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=worker_1, args=(2,))
#     p2 = multiprocessing.Process(target=worker_2, args=(3,))
#     p3 = multiprocessing.Process(target=worker_3, args=(4,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     print("The number of CPU is:" + str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print("child p.name:" + p.name +"\tp.id"+ str(p.pid))
#
#     print("END!!!!!!!!!!")

# class ClockProcess(multiprocessing.Process):
#     def __init__(self,interval):
#         multiprocessing.Process.__init__(self)
#         self.__interval = interval
#
#     def run(self):
#         n = 5
#         while n > 0:
#             print("the time is {0}".format(time.ctime()))
#             time.sleep(self.__interval)
#             n-=1
# if __name__ == '__main__':
#     p = ClockProcess(3)
#     p.start()

# 不加deamon属性
# def worker(interval):
#     print("work start:{0}".format(time.ctime()))
#     time.sleep(interval)
#     print("work end:{0}".format(time.ctime()))
#
# if __name__ == "__main__":
#     p = multiprocessing.Process(target=worker, args=(3,))
#     p.start()
#     print("end")
# 加deamon属性
# def worker(interval):
#     print("work start:(0)".format(time.ctime()))
#     time.sleep(interval)
#     print("work end:{0}".format(time.ctime()))
#
# if __name__ == "__main__":
#     p = multiprocessing.Process(target=worker, args=(3,))
#     p.daemon = True
#     p.start()
#     print("end !!!!!!!!")
# # 子进程设置了deamon属性,主进程结束,它们就随着结束了

# 设置deamon执行完结束的方法
# def worker(interval):
#     print("work start:{0}".format(time.ctime()))
#     time.sleep(interval)
#     print("work end:{0}".format(time.ctime()))
#
# if __name__ == "__main__":
#     p = multiprocessing.Process(target=worker, args=(3,))
#     p.daemon = True
#     p.start()
#     p.join()
#     print("end!!")
import sys,os
# def worker_with(lock, f):
#     with lock:
#         fs = open(f, 'a+')
#         n = 10
#         while n>1:
#             fs.write("Locked acquired via with\n")
#             n-=1
#         fs.close()
# def worker_no_with(lock,f):
#     lock.acquire()
#     try:
#         fs = open(f,'a+')
#         n = 10
#         while n > 1:
#             fs.write("Lock acquired directly\n")
#             n-=1
#         fs.close()
#     finally:
#         lock.release()
#
# if __name__ =="__main__":
#     lock = multiprocessing.Lock()
#     f = "file.txt"
#     w = multiprocessing.Process(target=worker_with, args=(lock,f))
#     nw = multiprocessing.Process(target=worker_no_with, args=(lock,f))
#     w.start()
#     nw.start()
#     print("end")

# def worker_with(lock, f):
#     with lock:
#         fs = open(f, 'a+')
#         n = 10
#         while n > 1:
#             fs.write("Lockd acquired via with\n")
#             n -= 1
#         fs.close()
#
#
# def worker_no_with(lock, f):
#     lock.acquire()
#     try:
#         fs = open(f, 'a+')
#         n = 10
#         while n > 1:
#             fs.write("Lock acquired directly\n")
#             n -= 1
#         fs.close()
#     finally:
#         lock.release()
#
#
# if __name__ == "__main__":
#     lock = multiprocessing.Lock()
#     f = "file.txt"
#     w = multiprocessing.Process(target=worker_with, args=(lock, f))
#     nw = multiprocessing.Process(target=worker_no_with, args=(lock, f))
#     w.start()
#     nw.start()
#     print("end")
# def worker(s,i):
#     s.acquire()
#     print(multiprocessing.current_process().name+"acquire")
#     time.sleep(3)
#     print(multiprocessing.current_process().name+"release")
#     s.release()
#
# if __name__ == "__main__":
#     s = multiprocessing.Semaphore(3)
#     for i in range(10):
#         p = multiprocessing.Process(target=worker, args=(s,i*2))
#         p.start()

# def wait_for_event(e):
#     print("wait_for_event:starting")
#     e.wait()
#     print("wairt_for_event:e.is_set()->"+str(e.is_set()))
#
# def wait_for_event_timeout(e, t):
#     print("wait_for_event_timeout:starting")
#     e.wait(t)
#     print("wait_for_event_timeout:e.is_set->" + str(e.is_set()))
#
# if __name__ == "__main__":
#     e = multiprocessing.Event()
#     w1 = multiprocessing.Process(name="block", target=wait_for_event,args=(e,))
#
#     w2 = multiprocessing.Process(name="non=block", target=wait_for_event_timeout,args=(e,5))
#     w1.start()
#     w2.start()
#
#     time.sleep(10)
#     # wait() 如果赋值则在时间后执行set依旧为False,不赋值则等到set改变其set值
#     e.set()
#     print("main: event is set")


def writer_proc(q):
    try:
        q.put(1, block = False)
    except:
        pass
def reader_proc(q):
    try:
        print(q.get(block=False))
    except:
        pass
if __name__ == "__main__":
    q = multiprocessing.Queue()
    writer = multiprocessing.Process(target=writer_proc, args=(q,))
    writer.start()

    reader = multiprocessing.Process(target=reader_proc, args=(q,))
    writer.join()
    reader.start()
    reader.join()

    writer.join()



