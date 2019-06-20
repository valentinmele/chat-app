import os
from PIL import Image


def check_size_and_format(im):
    formats = ["JPEG", "PNG", "GIF"]

    if im.format in formats:
        print("Format de l'image OK : ", im.format)
        if os.path.getsize(im.filename) < 2000000:
            print("Taille de l'image OK : ", os.path.getsize(im.filename))
            return True
        else:
            print("Image trop grande (>2mo)  KO : ", os.path.getsize(im.filename))
    else:
        print("Format non supporté KO : ", im.format)

    return False


def resize(default_img):
    if check_size_and_format(default_img):
        basewidth = 120
        wpercent = basewidth / float(default_img.size[0])
        hsize = int((float(default_img.size[1]) * float(wpercent)))
        img = default_img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save("resize-" + default_img.filename)


if __name__ == "__main__":
    im = Image.open("thomas.jpg")
    im2 = Image.open("2mo.jpg")

    resize(im)
