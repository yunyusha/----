import requests
"""

requests: 完成网络请求的模块
网络请求:服务器和客户端进行数据交互的过程
网络请求需要两部分内容:
网址(url): 用来帮助开发人员找到指定的服务器
参数: 用来告知服务器需要提供的服务内容,可以
保证服务器提供精准的服务

在网络请求中,有两个非常流行的请求方式,分别是:
GET和POST
GET: 客户端向服务器发送请求,把需要的数据一并传给服务器.因此GET请求
的网址和参数通过"?"组合在一起,此种方式不利于数据的安全.同时GET向服务器发送
最多288个字节的数据,因此数据传输量比较小
综上GET一般用来向服务器获取数据

POST:客户端向服务器先发送链接请求,链接成立之后,向服务器发送数据,因此POST
请求的网址和参数是分开的,这样可以保证数据的安全性.同时POST向服务器最多发送
5M的数据,数据传输量比较大 


"""
url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-08-08&leftTicketDTO.from_station=VAP&leftTicketDTO.to_station=ZZF&purpose_codes=ADULT"

result = requests.get(url)
# result.json(): 将网址返回的的json数据解析成当前语
# 言能够识别的数据格式(JSON解析),注意返回的数据必须是JSON
# 字符串
"""
JSON数据是前端和后台约定好的一种数据结构,该数据有[]{}
互相嵌套组成的一种字符串数据,JSON数据一般不能直接被某一种语言识别
需要通过JSON解析之后才能被识别
"""
print(result.json())

# response = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9061')
# data_str = response.text.strip('var station_names =;')
# data_list = data_str.split('@')[1:]
# data_dict = {}
# for item in data_list:
#     list_temp = item.split('|')
#     data_dict[list_temp[1]] = list_temp[2]
# print(data_dict)

