from PIL import Image
from random import randint


def paste_random_size_image(image_name):
    img = Image.open("elements/" + image_name + ".png")
    max_w, max_h = 256, 256
    img_w, img_h = img.size
    ration = min(max_w/img_w, max_h/img_h)
    percent = randint(10,101)/100
    img_w, img_h = int(img_w * ration * percent), int(img_h * ration * percent)
    size = img_w, img_h
    img.thumbnail(size, Image.ANTIALIAS)
    background.paste(img, (i, j), img)


elements = ["nebula_1", "nebula_2", "planet_1"]
background = Image.new('RGB', (1080, 720), "black")  # create a new black image
for i in range(background.size[0]):  # for every col:
    for j in range(background.size[1]):  # For every row
        rand = randint(0, 100000)
        if rand < len(elements):
            paste_random_size_image(elements[rand])

background.show()
