from PIL import Image
im = Image.open('xieyuan.jpg')
print(im.getbands())
print(im.mode)
print(im.size)
print(im.info)

im_bilinear = im.resize((866, 541), Image.BILINEAR)
im_bicubic = im.resize((866, 541), Image.BICUBIC)
im_antialias = im.resize((866, 541), Image.ANTIALIAS)

im_bilinear.save('bilinear.jpg', 'jpeg')
im_bicubic.save('bicubic.jpg', 'jpeg')
im_antialias.save('antialias.jpg', 'jpeg')
