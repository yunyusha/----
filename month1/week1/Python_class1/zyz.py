print('%')
# 控制台输入两个整数a,b,请输出a占b的百分之多少
num1 = int(input("请输入一个整数a"))
num2 = int(input("请输入一个整数b"))

per = 100*(num1/num2)
print("数字a占数字b的%.2f%%" % per)  # .2f为保留小数点后两位
