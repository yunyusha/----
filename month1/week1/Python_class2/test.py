# # 第四题 (星座)
# month = (input("请输入出生在几月份"))
# day = (input("请输入出生在几日"))
# rmonth = int(month)
#
# rday = int(day)
# if rday<10:
#     day = str(rday)
#     day = "0" + day
# bir = int(month + day)
#
# if rmonth>12 or rday>31:
#     print("输入错误")
# else:
#     if bir <= 419 and bir>=321:
#         print("白羊座")
#     elif bir <=520 and bir >=420 :
#         print("金牛座")
#     elif bir <=722 and bir >=622 :
#         print("巨蟹座")
#     elif bir <=822 and bir >=723:
#         print("狮子座")
#     elif bir <=1023 and bir >=923:
#         print("天秤座")
#     elif bir <=1122 and bir >=1024:
#         print("天蝎座")
#     elif bir <=218 and bir >=120:
#         print("水瓶座")
#     elif bir <=621 and bir >=521:
#         print("双子座")
#     elif bir <=922 and bir >=823:
#         print("处女座")
#     elif bir <=1221 and bir >=1123:
#         print("射手座")
#     elif bir <=320 and bir >=219:
#         print("双鱼座")
#     elif bir <=119 or bir >=1222:
#         print("摩羯座")
#
# num6_1 = int(input("请输入一个整数1"))
# num6_2 = int(input("请输入一个整数2"))
#
# if num6_1 > num6_2:
#     for i in range(num6_2, 0, -1):
#         if num6_1 % i == 0 and num6_2 % i == 0:
#             print("最大公约数是%d" % i)
#             break
#
# else:
#     for i in range(num6_1, 0, -1):
#         if num6_1 % i == 0 and num6_2 % i == 0:
#             print("最大公约数是%d" % i)
#             break
a = 1000
for i in range(1, a):
    a = a + 1
    jnum1 = int(input("请输入数字a"))
    jnum2 = int(input("请输入数字b"))
    shysf = int(input("请输入根据提示输入运算符1:+,2:*,3:/,4:-,5://,6:%"))

    if shysf==1:
        print(jnum2+jnum1)
    else:
        if shysf == 2:
            print(jnum1*jnum2)
        else:
            if shysf == 3 and jnum2!=0:
                print(jnum1/jnum2)
            else:
                if shysf == 4:
                    print(jnum1-jnum2)
                else:
                    if shysf == 5 and jnum2!=0:

                        print(jnum1//jnum2)
                    else:
                        if shysf == 6:
                            print(jnum1 % jnum2)
                        else:
                            print("错")
