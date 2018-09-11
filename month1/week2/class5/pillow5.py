from PIL import Image, ImageChops, ImageDraw, ImageFont
img = Image.open('img/1.jpg')
# 切换图片模式
img = img.convert('RGBA')
# 创建一个背景完全透明的图片模板,大小和原始图片一样大

w, h = img.size

new_img = Image.new('RGBA', (w, h), (0, 0, 0, 0))

# 使用ImageDraw生成一个画笔
# 此过程需要用户提前指定需要操作的图片

draw_1 = ImageDraw.Draw(new_img)
# 绘制文字
# 使用imageFont生成对应的字体
font = ImageFont.truetype('img/111.ttf', 50)

draw_1.text((100, 300), '啦啦啦啦啦', font=font, fill=(100, 101, 100))

new_img = new_img.rotate(45)
# 设置new_img向左下角移动
new_img = ImageChops.offset(new_img, -30, 30)
# new_img.show()
# 将文字和图片进行合并
combine_img = Image.alpha_composite(img, new_img)
combine_img.show()
# 图片保存
combine_img = combine_img.convert('RGB')
combine_img.save('kkk.jpg')

