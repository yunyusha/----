# 排序算法之:侏儒排序法
# 每次比较两个数
def gnomessort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i-=1

# 排序算法:归并排序法
def mergesort(seq):
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]  # [:mid]表示得到mid之前元素,不含mid[mid:]得到之后的元素,包含mid
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append((lft.opp()))
        else:
            res.append(rgt.opp())
    res.reverse()
    return (lft or rgt) + res