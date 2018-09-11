from PIL import Image, ImageDraw,ImageFilter,ImageFont
import random
# 生成随机验证码

def tupian():# 生成随机数,用于生成每个随机像素点
    x = random.randint(200, 255)
    y = random.randint(200, 255)
    z = random.randint(200, 255)
    return x, y, z
new_img = Image.new('RGB',(400, 200),tupian())# 建造一张图片
img2 = ImageDraw.Draw(new_img)# 作为画板
for x_1 in range(400):# 每个像素点生成随机颜色
    for y_1 in range(200):
        img2.point((x_1, y_1), fill=tupian())

def rndChar():# 生成随机字符
    x = random.randint(65, 90)
    return chr(x)
def rndColor():# 生成随机颜色用于字体的颜色
    x = random.randint(32, 127)
    y = random.randint(32, 127)
    z = random.randint(32, 127)
    return x, y, z
font = ImageFont.truetype('img/111.ttf',100)# 导入生成字符所用的随机字体
for m in range(4):# 生成四个随机颜色随机字符
    img2.text((80 * m + 70, 70), rndChar(), font=font,fill=rndColor())

new_img.show()