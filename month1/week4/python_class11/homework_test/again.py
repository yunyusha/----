# """DOC OPT
# USage:
#     doc_opt.py start
#     doc_opt.py [-gdzk] <from> <to> <time>
#
# Options:
#     -g  高铁
#     -d  动车
#     -k  普快
#     -z  直达
#     -t  特快
#
# """
# """
# docopt:用来帮助开发人员定义对应的终端运行指令集,当开发人员通过终端输入执行命
# 令时,此时docopt方法会自动根据指令完成对终端至零点匹配
#
# -abc 代表选择项,最终对应的结果是True或是False
# <from>:代表参数from,用来接受终端输入的参数数据
# []:代表里面的内容是可选的
# ():代表里面的内容是必选的
# a|b:代表a和b两种内容选择一种输入
# <from>...此时<from>代表可变参数,该参数对应的数据是一个列表,可以用来结束任
# 意多个参数数据
# """
# # []为可选,()为必选参数...为可变参数
# from docopt import docopt
# from prettytable import PrettyTable
# # 判断当前的文件是否正在被调用
# if __name__ == "__main__":
#     arguments = docopt(__doc__)
#     print(arguments)
#     # 创建表格对象
#     table = PrettyTable(['name', 'age', 'sex', 'birth'])
#     table.header_style = "cap"
#     table.align = "r"
#     table.add_row(['小刀刀', 22, '男', '2018-8-18'])
#     # 显示表格
#     print(table)

# import requests
# """
# requests:完成网络请求的模块
# 网络请求:服务器和客户端进行数据交互的过程
# 网络请求需要两部分内容:
# 网址(url):用来帮助开发人员找到指定的服务器
# 参数: 用来告知服务器需要提供的服务内容,可以保证
# 服务器提供精准的服务
#
# 在网络请求中,有两个非常流行的请求方式,分别是:
# GET 和 POST
# GET: 客户端向服务器发送请求,把需要的数据一并传给服务器,因此
# GET请求的网址和参数通过"?"组合在一起,此种方式不利于数据的安全
# 同时GET向服务器发送最多288个字节的数据,因此数据传输量比较小
# 综上GET一般用来向服务器获取数据
#
# POST:客户端向服务器先发送链接请求,链接成立之后,向服务器发送数据
# 因此POST请求的网址和参数是分开的,这样可以保证数据的安全性,同时
# POST向服务器最多发送5M的数据,数据传送量比较大
#
# """
# url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-08-08&leftTicketDTO.from_station=VAP&leftTicketDTO.to_station=ZZF&purpose_codes=ADULT"
# result = requests.get(url)
# """
# result.json():将网址返回的json数据解析成当前语言能够识别的数据格式(JSON解析),
# 注意返回的数据必须是JSON字符串
#
# JSON数据是前端和后台约定好的一种数据结构,该数据有[]{}互相嵌套
# 组成的一种字符串数据,JSON数据一般不能直接被某一种语言识别,
# 需要通过JSON解析之后才能被识别
#
# """
# print(result.json())

# import requests, os, json
# class Ticket(object):
#     def __init__(self, **kw):
#         self.__from = kw.get('from')
#         self.__to = kw.get('to')
#         self.__time = kw.get('time')
#         self.__station_VPN = self.get_station_vpn()
#
#     # 定义函数完成对车站VPN编号的获取
#     def get_station_vpn(self):
#         path = os.getcwd()+"/data"
#         if not os.path.exists(path):  # 如果该文件夹不存在
#             # 创建data文件夹
#             os.mkdir(path)
#             # 向服务器发起请求,并对返回数据进行处理
#             response = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9061')
#             # 去除字符串左右两端的指定字符,只获取''之间的内容
#             data_str = response.text.strip('var station_names =;')
#             # 将车站数据按照@符号分割
#             data_list = data_str.split('@')[1:]
#             # 将列表中的字符串再次处理最终转换成字典结构
#             data_dict={}
#             for item in data_list:
#                 list_temp = item.split('|')
#                 data_dict[list_temp[1]] = list_temp[2]
#
#             """
#             将处理后的数据转换成JSON字符串,写入到文件中,写入到文件中(json)
#             注意在Python中我们一般只对列表和字典进行json归档
#            """
#             data_str = json.dumps(data_dict)
#             # 将数据写入文件
#             file = open(path+"/data.txt", 'w')
#             file.write(data_str)
#             file.close()
#             return data_dict
#         else:
#             # 说明之前已经获取过VPN此时只需将数据读取出来即可
#             file = open(path+"/data.txt", 'r')
#             data_str = file.read()
#             file.close()
#             # 将读取到的数据做json解析
#             return json.loads(data_str)
#     # 定义方法完成车票查询操作
#     def check_ticket(self):
#         url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={time}&leftTicketDTO.from_station={from_st}&leftTicketDTO.to_station={to}&purpose_codes=ADULT".format(time=self.__time, from_st=self.__station_VPN.get(self.__from), to=self.__station_VPN.get(self.__to))
#         # 获取本次的查询结果
#         response = requests.get(url)
#         print(response.json())





