import time
# 获取时间戳
time1 = time.time()
time1 = time.localtime()
print(time1)

# 获取指定格式的时间

"""

%Y:年(四位)
%y:年(两位)
%m:月(01-12)
%d:日期(0-31)
%H:小时(24进制)
%I:小时(12进制)
%M:分钟(00-59)
%S:秒(00-59)
%a:简化版的星期几
%A:本地星期的全称
%d:本地月份的简称
%B:本地月份的全称
%p:输出时间的上下午简称
%j:获取当前指定时间为该年的第几天
%D:年月日的简写
%c:以简化版的格式输出日期
"""

date = time.strftime('%c %Y-%y %m %d %H %I ', time1)
date1 = time.strftime('%M %S %a %A %d %B %p %j %D ', time1)
# date = '%Y-%m-%d %H:%M:%S'
print(date)
print(date1)
# 设置程序休眠
time.sleep(30)
print('程序休眠结束')
