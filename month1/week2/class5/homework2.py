#coding:utf-8
from PIL import Image

#要索引的字符列表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)

 #读取图像文件
def readImg():
    img = Image.open('img/2.png')
    (width, height) = img.size
    img = img.resize((int(width * 0.9),  int(height * 0.5)))
    print(img.size)
    return img

def convert(img):
    # 转为灰度图像
    img = img.convert('L')
    txt = ''
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            # 获取每个坐标像素点的灰度
            gray = img.getpixel((x, y))
            unit = 256.0 / length
            txt += ascii_char[(int)(gray/unit)]
        txt += '\n'
    return txt
txt = convert(readImg())
with open('kai.txt', 'w') as f:
        f.write(txt)
