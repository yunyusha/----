from PIL import Image, ImageFilter
img = Image.open('img/1.jpg')
img.show()
# 为图片添加滤镜
# img = img.filter(ImageFilter.GaussianBlur(radius=10))
# 分离图像通道
r, g, b = img.split()
# 将红色和蓝色通道调换,
# 将指定的多个单通道颜色值进行合并

"""
分离图像通道分离之后得到的是三个单通道的image图像

merge(mode,(r, g, b,)):mode代表以何种模式进行合并,
rgb分别代表三种颜色的通道图像值
"""
b = b.point(lambda x:x*1.5)
img = Image.merge(img.mode, (g, b, r))

img.show()

