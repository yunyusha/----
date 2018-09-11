from PIL import Image, ImageChops


image1 = Image.open('img/2.png')
image2 = Image.open('img/3.png')

# 将图片image1向右上移动
# offser (img,x,y)将图片img沿x方向y方向移动x中正值往右移动
# 沿y方向,正值向下移动负值向上移动
image1 = ImageChops.offset(image1, 100, -10)

w1, h1 = image1.size
w2, h2 = image2.size
print(w1, h1)
print(w2, h2)
# 将图片img2 缩小成和img1一样大

image2 = image2.resize((w1, h1))

# 将图片image1与image2进行合并
# blend 将两张图片合并到一起,但是需要用户提供
# 一个alpha之后计算机会计算另一张图片透明度
# 然后进行图片的合并
new_img = Image.alpha_composite(image2, image1)
# 调整图片每个像素点的亮度
# new_img = new_img.point(lambda x: 1.2*x)

# new_img = Image.blend(image2, image1, 0.5)
new_img.show()
new_img.save('img/combine.png')
