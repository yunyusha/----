#
#
# num = []
# for i in range(10):
#     num.append(i)
# print(num)
# num5 = num
# num_s = []
# zz= []
# for i5 in range(len(num5)):
#     num_5 = [0,1,2,3,4,5,6,7,8,9]
#     for i_5 in range(len(num_5)):
#         num__5 = [0,1,2,3,4,5,6,7,8,9]
#         for i__5 in range(len(num__5)):
#             sum_6 = (num5[i5] ** 3) + (num_5[i_5] ** 3) + (num_5[i_5] ** 3)
#             if sum_6>=100 and sum_6<=999:
#                 print(sum_6)
#
#
#     print(zz)
#
# print(num_s)

n7 = int(input("请输入人数"))
num7 = []
num_7 =[]
for i7 in range(1, n7+1):
    num7.append(i7)
# print(num7)
# i_7 = 0
# while num7 != []:
#     if i_7+2 < n7:
#         re = num7.pop(i_7+2)
#
#         num_7.append(re)
#
#     elif i_7+2 == n7:
#         i_7 = -2
#         re = num7.pop(0)
#
#         num_7.append(re)
#     elif i_7+1 == n7:
#         re = num7.pop(n7-1)
#         i_7 = 1
#         num_7.append(re)
#     elif i_7 == n7:
#         re = num7.pop(n7-1)
#         num_7.append(re)
#         i_7 = -1
#     else:
#         re = num7.pop(0)
#         num_7.append(re)
#     i_7 = i_7 + 2
#     n7 = n7 - 1
# print(num_7)
#
#

print(num7)
i_7 = 0
while num7 != []:
    if i_7+2 < n7:
        re = num7.pop(i_7+2)

        num_7.append(re)

    elif i_7+2 == n7:
        i_7 = -2
        re = num7.pop(0)

        num_7.append(re)
    elif i_7+1 == n7:
        re = num7.pop(1)
        i_7 = 1
        num_7.append(re)
    elif i_7 == n7:
        if n7 > 2:
            re = num7.pop(2)
            num_7.append(re)
            i_7 = i_7-3
            n7 = n7 + 3
        else:
            re = num7.pop(0)
            num_7.append(re)
            i_7 = -1
    else:
        re = num7.pop(1)
        num_7.append(re)
        i_7 = -1

    i_7 = i_7 + 2
    n7 = n7 - 1
print(num_7)


