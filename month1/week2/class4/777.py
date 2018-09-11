
# import re

# def count_7(str_7): # 统计出其中英文字母、空格、数字和其它字符的个数
#     enum = re.findall(r'[a-zA-Z]{1}', str_7)
#     kong = re.findall(r'[ ]', str_7)
#     shu = re.findall(r'\d', str_7)
#     other = re.findall(r'[^\s\w]', str_7)
#     print(enum)
#     print(len(enum))
#     print(kong)
#     print(len(kong))
#     print(shu)

#     print(len(shu))
#     print(other)
#     print(len(other))
# text = count_7('sddg onj 3      25\--asf1')
# list1 = [0,1]
def fb(n,list1=[]):
    if n == 1:
        list1.append(0)
        return list1
    elif n == 2:
        list1.append(0)
        list1.append(1)
        return list1
    else:
        # list1 = fb(n-2, list1)
        list1 = fb(n-1, list1)
        num = list1[n-3] + list1[n-2]
        list1.append(num)
        return list1

print(fb(7))