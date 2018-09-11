import threading

# 递归锁(相对于lock更加高级的锁)
"""

在开发过程中不建议使用lock,因为同一个线程在使用lock同时获取多次锁时,会出现程旭堵塞现
象,因此开发中为了避免该种情况,建议使用RLock,(递归锁)

"""
lock = threading.RLock()
# 创建锁对象
# lock = threading.Lock()
print("程序准备要锁")
lock.acquire()
print("程序上锁")
lock.acquire()
print("程序再次上锁")
print("程序锁定")
lock.release()
lock.release()

