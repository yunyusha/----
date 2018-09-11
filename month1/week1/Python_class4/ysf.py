# 第七题 控制台输入n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。从编号为1的人开始报数，
# 数到3的那个人出列；出列人的下一个人又从1开始报数，数到3的那个人又出列；依此规律重复下去，直到
# 圆桌周围的人全部出列，请依次输出对应的出列顺序
n = int(input("请输入人数"))
list1 = [0 for i in range(n)]
count = index = 0
# count 存储当前游戏者所报数字,index存储当前是第几个游戏者报的数字
while list1.count(0)> 1:
    if list1[index] == 0:
        count += 1
        if count == 3:
            list1[index] = 1
            print("编号为%d的游戏者出圈" % (index+1))
            count = 0
    index += 1
    if index == n:
        index = 0
print(list1.index(0)+1)