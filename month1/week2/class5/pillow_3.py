from PIL import Image
image1 = Image.open('img/1.jpg')
# image1.show()

w, h = image1.size
# 创建一个透明模板
new_img = Image.new('RGBA', (w, h), (0, 0, 0, 0))

# 获取指定图片所有像素点
for x in range(w):
    for y in range(h):
        r, g, b = image1.getpixel((x, y))
        # 判断当前位置的像素点是否是白色的
        if 255 >= r >= 253 and 255 >= g >= 253 and 255 >= b >= 253:
            pass
        else:
            # 将对应位置非白色的像素点转移到新的图片模板里面
            new_img.putpixel((x, y), (r, g, b))
# 保存指定的图片,将图片保存成缩略图的格式
new_img.show()
new_img.save('img/new_img.oop', 'png')
