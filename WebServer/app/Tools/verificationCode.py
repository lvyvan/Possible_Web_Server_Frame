from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def verify_code():
    import random
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    im = Image.new('RGB', (width, height), bgcolor)
    draw = ImageDraw.Draw(im)
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值 删除易混淆的 0 / o
    str1 = 'ABCD123EFGHIJK456LMNPQRS789TUVWXYZabcdefhijkmnprstuvwxyz'
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    # /usr/share/fonts/truetype/dejavu
    font = ImageFont.truetype('DejaVuSans.ttf', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    del draw
    buf = BytesIO()
    im.save(buf, 'png')
    imgb = buf.getvalue()
    del buf
    return  rand_str, imgb

if __name__ == "__main__":
    print(verify_code())
