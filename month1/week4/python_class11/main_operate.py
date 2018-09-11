"""Main Operate
Usage:
    main_operate.py [-gkdtz] <from> <to> <time>
    main_operate.py [-GDKTZ] <from> <to> <time>

Options:

"""
from docopt import docopt
from tickets import Ticket
import time
if __name__ == "__main__":
    arguments = docopt(__doc__)
    # 根据用户输入的选择项完成对应类别列车的信息查询
    kinds = []
    if arguments.get("-g") is True or arguments.get("-G") is True:
        kinds.append('G')
    if arguments.get("-k") is True or arguments.get("-K") is True:
        kinds.append("K")
    if arguments.get("-d") is True or arguments.get("-D") is True:
        kinds.append("D")
    if arguments.get("-t") is True or arguments.get("-T") is True:
        kinds.append("T")
    if arguments.get("-z") is True or arguments.get("-Z") is True:
        kinds.append("Z")
    if len(kinds) == 0:
        kinds = ["K","G", "D", "T", "Z"]
    # 获取当前程序运行时的时间
    time_date = time.strftime("%Y-%m-%d", time.localtime())
    # 获取用户通过终端输入的时间
    time_input = arguments.get("<time>").split('-')
    # 将用户输入的日期变成两位表示
    time_input = list(map(lambda x: ("0"+x) if len(x) == 1 else x, time_input))
    time_input = "-".join(time_input)
    # 判断用户输入的时间是否超出12306查询时间
    if time_input >= time_date:
        dic = {'from':arguments.get('<from>'), "to":arguments.get('<to>'),'time':time_input}
        ticket = Ticket(**dic)
        ticket.check_ticket()
        ticket.check_train(kinds)
    else:
        print('对不起您所查询的列车时间不在规定时间之内')


