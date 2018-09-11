import os
"""
os:python内置的文件和文件加操作模块 
"""
# 获取当前文件工作的目录(该目录只包含文件夹)
path = os.getcwd()
print(path)
# 修改当前工作的目录
os.chdir(os.getcwd()+"/img")
print(os.getcwd())
file = open('aa.txt', 'w', encoding='utf8')
file.write('测试数据')
file.close()
# 获取指定路径中所用的文件列表
list_dirs = os.listdir('..')
print(list_dirs)

# 创建文件夹
# os.mkdir(os.getcwd()+"/imgs")
# 递归创建文件夹
# os.makedirs(os.getcwd()+'/a/b/c/d')
# 删除文件夹
# os.removedirs(os.getcwd()+'/a/b/c/d')


# 定义函数完成指定路径下文件夹的删除
def remove_dir(path):
    # 获取指定路径下所有的文件或者文件夹
    list_dirs = os.listdir(path)
    for file_name in list_dirs:
        # 判断当前指定路径下的文件是否是文件或者是文件夹
        if os.path.isfile(path+'/'+file_name):
            # 删除普通文件
            os.remove(path+'/'+file_name)
        else:
            remove_dir(path+'/'+file_name)
            # 删除一个文件夹
            os.rmdir(path+'/'+file_name)

remove_dir('C:/Users/lanouhn/Desktop/Python_basic/Python_class8/Python_class8/sss')

# 文件夹重命名(rename):帮助开发人员进行文件或文件夹的重命名

# result = os.rename('112123.jpg','3.jpg')
# print(result)

# 获取指定路径下文件夹或文件信息
print(os.stat('3.jpg').st_size)

# 专门获取指定文件的尺寸
print(os.path.getsize('3.jpg'))
# 路径分割(split()直接将指定的文件路径分割成文件夹和文件两部分)
result = os.path.split(os.getcwd()+'/3.jpg')
print(result)
# 该方法会将文件分为两部分,一部分是文件后缀,主要用来获取文件后缀名
result = os.path.splitext(os.getcwd()+"/3.jpg")
print(result)
# 路径拼接
path = os.path.join(os.getcwd(),'8.jpg')
print(path)
# 判断指定的路径下的文件是文件类型还是文件夹
result = os.path.isdir(os.path.join(os.getcwd(), '3.jpg'))
print(result)
# 判断指定路径是否是连接类型
result = os.path.islink('https://www.baidu.com/?tn=98050039_dg&ch=1')
print(result)
import re
path = 'http://www.baidu.com'
if re.match('http[s]?:', path) is not None:
    print('是连接')
else:
    print('不是链接')
# 判断某个路径是否是真实存在
result = os.path.exists(os.path.join(os.getcwd(), '3.jpg'))
print(result)

# # 判断指定目录下面的两个文件是否是同一文件
# path = 'C:\Users\lanouhn\Desktop\Python_basic\month1\week4\python_class10\img\3.jpg'
# os.path.samefile('C:\Users\lanouhn\Desktop\Python_basic\month1\week4\python_class10\img\3.jpg')
# print(result)
# 操作系统PATH路径
path = os.getenv('Path')
print(path)
# 设置系统环境变量(临时设置环境变量,只对当前脚本起作用)
os.putenv('Path', 'C:\\root')





