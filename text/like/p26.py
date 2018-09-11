a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e, f},  # a
    {c, e},           # b
    {d},              # c
    {e},              # d
    {f},              # e
    {c, g, h},        # f
    {f, h},           # g
    {f, g}            # h
]
print(b in N[a])  # 相邻节点 Neighborhood membership
print(len(N[f]))  # 度 Degree
