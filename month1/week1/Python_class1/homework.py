# 第一题
num = input("请输入\n")
print(num)

# 第二题
money = input("请输入金额")
money = int(money)
i100 = money//100
money = money - i100 * 100
i50 = money // 50
money = money - i50*50
i10 = money // 10
money = money - i10*10
i5 = money // 5
money = money - i5*5
i1 = money // 1

print("共需要100元%d张,50元%d张,10元%d张,5元%d张,1元%d张" % (i100, i50, i10, i5, i1))

# 第三题
num1 = input("请输入整数1")
num2 = input("请输入整数2")
num1 = int(num1)
num2 = int(num2)
numh = num1 + num2
numc = num1 - num2
numx = num1 * num2
nums = num1 / num2
numy = num1 % num2
print("和%d\n差%d\n乘%d\n商%d\n余%d," % (numh, numc, numx, nums, numy))

# 第四题
zifu = input("请输入一个字符:")
print(zifu+"的Ascll码是%d" % ord(zifu))

# 第五题
Num = input("请输入一个数字")
Num = int(Num)
print(Num, "的整数对应的字符是%s" % chr(Num))

# 最后一题
num3 = input()
num4 = input()
num3 = int(num3)
num4 = int(num4)
num3 = num3 ^ num4
num4 = num3 ^ num4
num3 = num3 ^ num4
print(num3)
print(num4)
