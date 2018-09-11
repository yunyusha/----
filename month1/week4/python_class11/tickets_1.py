import os, requests, json, prettytable
class Ticket(object):
    def __init__(self, **kw):
        self.__table = prettytable.PrettyTable(["车次", "出发站/到达站", "出发时间/到达时间","历时", "商务座/特等座", "一等座", "二等座", "软卧", '硬卧', "硬座", "无座"])
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
            # 向服务器发起请求并且对返回数据进行处理
            response = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9061')
            # 去除字符串左右两端指定的字符，只获取''之间的内容
            data_str = response.text.strip('var station_names =;')
            # 将车站数据按照@符号进行分割
            data_list = data_str.split('@')[1:]
            # 将列表中的字符串再次处理最终转换成字典结构
            data_dict = {}
            for item in data_list:
                list_temp = item.split('|')
                data_dict[list_temp[1]] = list_temp[2]
            # 将处理之后的数据转换成JSON字符串，写入到文件中(json归档,注意在Python中我们一般只对列表和字典才能进行json归档)
            data_str = json.dumps(data_dict)
            # 将数据写入到文件
            file = open(path+"/data.txt", 'w')
            file.write(data_str)
            file.close()
            return data_dict
        else:
            # 说明之前的已经获取过VPN，此时只需将数据读取出来即可
            file = open(path+"/data.txt", 'r')
            data_str = file.read()
            file.close()
            # 将读取到的数据做json解析
            return json.loads(data_str)

    # 定义方法完成车票查询操作
    def check_ticket(self):
        url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={time}&leftTicketDTO.from_station={from_st}&leftTicketDTO.to_station={to}&purpose_codes=ADULT".format(time=self.__time, from_st=self.__station_VPN.get(self.__from), to=self.__station_VPN.get(self.__to))
        # 获取对应的余票信息
        # 设置header向服务器声明本次请求来源于浏览器
        header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.160 Safari/537.22"}
        response = requests.get(url, headers=header)
        data_json = response.json()
        self.__data_list = data_json.get('data').get('result')
    # 定义函数完成K字开头的列车信息查询,kinds列表类型的参数用来存储
    # 需要查询的列车类别,比如['K',"G"]:查询普快和高铁
    def check_train(self):
        for item in self.__data_list:
            list1 = item.split("|")[2:]
            if list1[1].find('K') != -1:
                # 根据当前车站的VPN编号获取对应车站信息
                from_st, to_st = self.check_station(list1[2:7])
                # 获取历时信息
                if list1[9] == "Y":
                    time_infor = str(list1[8])+"\n"+"当日到达"
                else:
                    time_infor = str(list1[8]) + "\n" + "次日到达"
                # 将本次列车信息添加到表格中
                self.__table.add_row([list1[1], from_st+"\n"+to_st, str(list1[6])+"\n"+str(list1[7]), time_infor, '--', '--', '--', list1[21], list1[26], list1[27], list1[24]])
        print(self.__table)

    # 定义函数完成车站信息的查询
    def check_station(self, list_vpn):
        from_st = to_st = ""
        if list_vpn[0] == list_vpn[2]:
            from_st += "始 "
        else:
            from_st += "过 "
        if list_vpn[1] == list_vpn[3]:
            to_st += "终 "
        else:
            to_st += "过 "
        dic = {}
        for key, value in self.__station_VPN.items():
            dic[value] = key
        from_st += dic.get(list_vpn[2])
        to_st += dic.get(list_vpn[3])
        return (from_st, to_st)



