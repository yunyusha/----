def jiecheng(n1):
    if n1 == 1:
        return 1
    else:
        return n1*jiecheng(n1-1)
result = jiecheng(12)