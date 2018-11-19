from PIL import Image
from random import randint, uniform
import numpy as np


def gravity(array, x, y):
    step_x = x / 10
    step_y = y / 10
    # put value of 1 on random positions in an array
    for i in range(0, y, step_y):  # for every row:
        for j in range(0, x, step_x):  # for every column
            if uni_array[i][j] == 1:
                pass


def gravity2():
    step_x = x // 300
    # if remainder, place offset here : for n in range(step_y):...
    step_y = y // 300
    # put value of 1 on random positions in an array
    for i in range(0, y - step_y + 1, step_y):  # for every row:
        for j in range(0, x - step_x + 1, step_x):  # for every column
            all_full = True
            for m in range(step_x):
                for n in range(step_y):
                    if uni_array[i + n][j + m] == 0:
                        all_full = False
            if all_full:
                total = 0
                for m in range(step_x):
                    for n in range(step_y):
                        total += uni_array[i + n][j + m]
                        if m != 0 or n != 0:
                            uni_array[i + n][j + m] = 0
                uni_array[i][j] = total
            else:
                for m in range(step_x):
                    for n in range(step_y):
                        uni_array[i + n][j + m] = 0


def gravity3():
    step_x = x // 10
    # if remainder, place offset here : for n in range(step_y):...
    step_y = y // 10
    # put value of 1 on random positions in an array
    for i in range(0, y - step_y + 1, step_y):  # for every row:
        for j in range(0, x - step_x + 1, step_x):  # for every column
            total = 0
            for m in range(step_x):
                for n in range(step_y):
                    total += uni_array[i + n][j + m]
                    uni_array[i + n][j + m] = 0
            uni_array[i][j] = total


def enlarge_star(rand_y, rand_x):
    star_size = uni_array[rand_y][rand_x]
    print(star_size)
    star_radius = (star_size / 3.14) ** (1 / 2)
    for i in range(y):  # for every row:
        for j in range(x):  # for every column
            dist = distance(rand_y, rand_x, i, j)
            rand = uniform(star_radius * 0.99, star_radius * 1.01)
            if 0 < dist < rand:
                uni_array[i][j] = -dist
    uni_array[rand_y][rand_x] = -1


def create_stars(strength, stars_number):
    stars = []
    for i in range(stars_number):
        rand_x = randint(0, x)
        rand_y = randint(0, y)
        uni_array[rand_y][rand_x] = 0
        stars.append((rand_y, rand_x))
    print(stars)
    for i in range(y):  # for every row:
        for j in range(x):  # for every column
            for t in stars:
                dist = distance(t[0], t[1], i, j)
                rand = randint(strength * (5 / 8), strength * (11 / 8))
                if 0 < dist < rand and uni_array[i][j] >= 0:
                    uni_array[t[0]][t[1]] += uni_array[i][j]
                    uni_array[i][j] = 0
    for t in stars:
        enlarge_star(t[0], t[1])


def distance(y1, x1, y2, x2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    return dist


def set_random_points(probability):
    # put value of 1 on random positions in an array
    for i in range(y):  # for every row:
        for j in range(x):  # for every column
            rand = randint(0, probability)
            if rand == 0:
                uni_array[i][j] = 1


def draw_image():
    for i in range(y):  # for every row:
        for j in range(x):  # for every column
            if uni_array[i][j] == 1:  # color the pixel is there is a value in array
                rand = randint(0, 1)
                if rand == 0:
                    pixels[j, i] = (0, 0, 255)
                else:
                    pixels[j, i] = (0, 255, 255)
            elif uni_array[i][j] < 0:
                pixels[j, i] = (255, 255 + uni_array[i][j], 255 + 7 * uni_array[i][j])
            else:
                pixels[j, i] = (0, 0, 0)


#  create an array to represent matter in universe
resolution = (1080, 720)
x = resolution[0]
y = resolution[1]
uni_array = [[0 for i in range(x)] for j in range(y)]
uni_array = np.array(uni_array)
background = Image.new('RGB', resolution, "black")  # create a new black image
pixels = background.load()

set_random_points(5)
create_stars(80, 2)

draw_image()
background.show()
# background.save("uni" + str(i) + ".png")
