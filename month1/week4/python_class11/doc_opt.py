"""DOC OPT
USage:
    doc_opt.py start
    doc_opt.py [-gdkzt] <from> <to> <time>


Options:
    -g   高铁
    -d   动车
    -k   普快
    -z   直达
    -t   特快
"""
"""
docopt:用来帮助开发人员定义对应的终端运行指令集,当开发人员通过终端输入执行命令是,此时docopt方法
会自动根据指令完成对终端指令的匹配
 
-abc 代表选择项,最终对应的结果是True或是False
<from>:代表参数from,用来接受终端输入的参数数据
[]:代表里面的内容是可选的
():代表里面的内容是必须的
a|b:代表a和b两种内容选择一种输入
<from>...此时<from>代表可变参数,该参数对应的数据是一个列表,可以用来接受任意多个参数数据

"""
# []为可选,()为必选参数 ...为可变参数
from docopt import docopt
from prettytable import PrettyTable
# 判断当前的文件是否正在被调用
if __name__ == "__main__":
    arguments = docopt(__doc__)
    print(arguments)
    # 创建表格对象
    table = PrettyTable(['name', 'age', 'sex', 'birth'])
    table.header_style = "cap"
    table.align = "r"
    table.add_row(['小呆呆', 20, '男', '2018-8-19'])
    # 显示表格
    print(table)
