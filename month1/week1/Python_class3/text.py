# import random
# num5 = [1, 2, 3, 4]
#
#
# num_s = []
#
# for i5 in range(len(num5)):
#     num_5 = [1, 2, 3, 4]
#     num_5.remove(num5[i5])
#     for i_5 in range(len(num_5)):
#         num__5 = [1, 2, 3, 4]
#         num__5.remove(num_5[i_5])
#         num__5.remove(num5[i5])
#         for i__5 in range(len(num__5)):
#
#             num_s.append([num5[i5], num_5[i_5], num__5[i__5]])
# print(num_s)
# for ii5 in range(len(num_s)):
#     for ii_z in range(len(num_s[ii5])):
#         ii_1 = str(num_s[ii5][ii_z])
#         sum_5 = int(ii_1)
#         print(ii_1, end="")
#     print("")
# print(len(num_s))

# for i5 in range(4):
#     num_5 = [1, 2, 3, 4]
#     num_5.remove(num5[i5])
#     print(num_5)
num = []
for ii6 in range(10):
    num.append(ii6)
# print(num)
num6 = num
num_6 = num
num__6 = num
# print(num_6)
result = []
for i6 in range(len(num6)):
    num_6 = num
    for i_6 in range(len(num_6)):
        num__6 = num
        for i__6 in range(len(num__6)):

            sum_6 = (num6[i6]**3)+(num_6[i_6]**3)+(num_6[i__6]**3)

            sum_sum = str(num6[i6])+str(num_6[i_6])+str(num_6[i__6])
            sum_int = int(sum_sum)
            if sum_6>=100 and sum_6<=999:
                # print(sum_6)
                if sum_6 == sum_int:
                    result.append(sum_6)

print(result)

