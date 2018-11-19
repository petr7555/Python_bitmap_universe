from PIL import Image
from random import randint, uniform
import numpy as np


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


def on_ellipse(ab, ey, ex, fy, fx, i, j):
    eb = distance(ey, ex, i, j)
    fb = distance(fy, fx, i, j)
    if eb + fb < ab:
        return True
    return False


def enlarge_galaxy(ab, ey, ex, fy, fx):
    # surface
    s = uni_array[ey][ex]
    # middle = ((ey + fy)/2, (ex + fx)/2)
    # es = distance(ey, ex, middle[0], middle[1])
    # distance from focus to the middle
    es = distance(ey, ex, fy, fx) / 2
    a = ab / 2
    b = (a ** 2 - es ** 2) ** (1 / 2)
    surface = 3.14 * a * b
    new_surface = uni_array[ey][ex]
    ratio = new_surface / surface
    new_a = a * ratio
    new_b = b * ratio
    ab = 2 * new_a
    star_radius = (s / 3.14) ** (1 / 2)
    for i in range(y):  # for every row:
        for j in range(x):  # for every column
            dist = distance(rand_y, rand_x, i, j)
            rand = uniform(star_radius * 0.99, star_radius * 1.01)
            if 0 < dist < rand:
                uni_array[i][j] = -dist
    uni_array[ey][ex] = -333
    uni_array[fy][fx] = -333


def create_galaxy(galaxies_number):
    galaxies = []
    for i in range(galaxies_number):
        # create two random focal points
        ex = randint(0, x)
        ey = randint(0, y)
        rand = randint(50, 100)
        fx = ex + rand
        rand = randint(-50, 50)
        fy = ey + rand
        rand = uniform(1.1, 1.3)
        ab = distance(ey, ex, fy, fx) * rand
        uni_array[ey][ex] = 0
        uni_array[fy][fx] = 0
        galaxies.append((ab, ey, ex, fy, fx))
    for i in range(y):  # for every row:
        for j in range(x):  # for every column
            for t in galaxies:
                ab = t[0]
                rand = randint(ab * (5 / 8), ab * (11 / 8))
                if on_ellipse(rand, t[1], t[2], t[3], t[4], i, j) and uni_array[i][j] >= 0:
                    uni_array[t[1]][t[2]] += uni_array[i][j]
                    uni_array[i][j] = 0
    for t in galaxies:
        enlarge_galaxy(t[0], t[1], t[2], t[3], t[4], )


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
            elif uni_array[i][j] == -3333:
                pixels[j, i] = (255, 0, 255)
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
# create_stars(80, 2)
create_galaxy()
draw_image()
background.show()
# background.save("uni" + str(i) + ".png")
