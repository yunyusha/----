# def clac_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax

# 调用此函数时返回的不是求和结果,而是求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
l = f()
print(l)
