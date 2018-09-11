import os, requests, json, prettytable
class Ticket(object):
    def __init__(self, **kw):
        self.__table = prettytable.PrettyTable(
            ["车次",
             "出发站/到达站",
             "出发时间/到达时间",
             "历时",
             "商务座/特等座",
             "一等座",
             "二等座",
             "高级软卧",
             "软卧",
             "硬卧",
             "硬座",
             "无座"
             ]
        )
        self.__from = kw.get('from')
        self.__to = kw.get('to')
        self.__time = kw.get('time')
        self.__station_VPN = self.get_station_vpn()

        # 存储未来查询到的所有列车信息
        self.__data_list = []
    # 定义函数完成车站VPN编号的获取
    def get_station_vpn(self):
        path = os.getcwd()+"/data"
        if not os.path.exists(path):
            # 创建data文件夹
            os.mkdir(path)
            # 向服务器发起请求并且返回数据进行处理
            response = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9061')
            # 去除字符串左右两端指定的字符,只获取''之间的内容
            data_str = response.text.strip('var station_names =;')
            # 将车站数据按照@符号进行分割
            data_list = data_str.split('@')[1:]
            # 将列表中的字符串再次处理最终转换成字典结构
            data_dict = {}
            for item in data_list:
                list_temp = item.split('|')
                data_dict[list_temp[1]] = list_temp[2]
            # 将处理之后的数据转换成JSON字符串,写入到文件中(json归档,注意在Python中我们一般只对列表和字典才能进行json归档)
            data_str = json.dumps(data_dict)
            # 将数据写入到文件
            file = open(path+"/data.txt",'w')
            file.write(data_str)
            file.close()
            return data_dict
        else:
            # 说明之前的已经获取VPN,此时只需将数据读取出来即可
            file = open(path+"/data.txt", 'r')
            data_str = file.read()
            file.close()


