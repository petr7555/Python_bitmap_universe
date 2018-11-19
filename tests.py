from PIL import Image
from random import randint
import numpy as np

resolution = (100, 500)
background = Image.new('RGB', resolution, "black")  # create a new black image
pixels = background.load()


def draw_image():
    for i in range(500):  # for every row:
        for j in range(100):  # For every column
            if j == 1:  # color the pixel is there is a value in array
                pixels[j, i] = (0, 0, 255)
            else:
                pixels[j, i] = (0, 0, 0)

draw_image()
background.show()
