from PIL import Image
img1 = Image.open('img/1.jpg')

# 截取图片中指定的区域
w, h = img1.size
area = ((w//2-100, 50, w//2+100,250))
# 开始截取
jp = img1.crop(area)
# 对截取图像做翻转
jp = jp.transpose(Image.ROTATE_180)
# 将截取的图像粘贴到原图像中
img1.paste(jp, area)
# img1.show()

# 创建一张新图片
new_img = Image.new('RGBA', (200, 200), (255, 255, 255, 1))
for x in range(200):
    for y in range(200):
        """
        getpixel image内部的方法,用来获取指定坐标(x,y)位置
        的像素值,putpiexl((x,y),color)用来指定的color放在
        指定的位置(x,y)处
        """

        r,g,b = jp.getpixel((x, y))
        if r <252 and g > 252 and b > 252:
            pass
        else:
            new_img.putpixel((x, y), (r, g, b))

new_img.show()
new_img.save('img/new_img.png')
