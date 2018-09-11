from PIL import Image
# 打开一张图片
img = Image.open('img/1.jpg')
# 获取图片的额外信息
print(img.format, img.size, img.mode)

# 转换图像模式(mode)
img = img.convert('L')# 转换成单通道图片

# 获取图片的所用像素点,point :获取图片对应的每一个像素点的值
# 并且,以回调函数的形式将每一个像素点的值返回给开发人员进行
# 数据处理3236
img = img.point(lambda x: 1.2*x if x < 200 else 0.1*x)

# 对图像进行缩放处理
w, h = img.size
img = img.resize((w//2, h//2))
# 旋转图片 rotate(angle,filter,expand
# angle代表旋转角度,filter代表一中滤镜效果,
# expand设置为一,此时图像在旋转过程中计算机会自动放
# 大图像保证旋转之后的图片在整个区域显示)
# img = img.rotate(-45, Image.BICUBIC, 1)

# 图像等比例缩放 thumbnail直接对图像进行缩放,
# 需要指定缩放之后的宽度和高度,同时指定缩放时
# 使用的滤镜效果
img.thumbnail((w//2, h//2), Image.ANTIALIAS)
# 图像变换
img = img.transpose(Image.ROTATE_90)


# 显示一张图片
img.show()




# 将处理之后的图像保存到指定的目录
img.save('C:/Users/lanouhn/Desktop/12.jpg')

