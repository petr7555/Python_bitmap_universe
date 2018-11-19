from PIL import Image
from random import randint, uniform
import numpy as np


def enlarge_star(rand_y, rand_x):
    star_size = uni_array[rand_y][rand_x]
    print("Creating star", star_size)
    star_radius = (star_size / 3.14) ** (1 / 2)
    for i in range(Y):  # for every row:
        for j in range(X):  # for every column
            dist = distance(rand_y, rand_x, i, j)
            rand = uniform(star_radius * 0.98, star_radius * 1.02)
            if 0 < dist < rand:
                uni_array[i][j] = -dist
    uni_array[rand_y][rand_x] = -1


def create_stars(size, stars_number = 1):
    stars = []
    for i in range(stars_number):
        rand_x = randint(0, X - 1)
        rand_y = randint(0, Y - 1)
        uni_array[rand_y][rand_x] = 0
        stars.append((rand_y, rand_x))
    for i in range(Y):  # for every row:
        for j in range(X):  # for every column
            for t in stars:
                dist = distance(t[0], t[1], i, j)
                rand = uniform(size * (5 / 8), size * (11 / 8))
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
    print("Creating galaxy", ab)
    middle_y = (ey + fy) / 2
    middle_x = (ex + fx) / 2
    new_ey = (ey + middle_y) / 2
    new_ex = (ex + middle_x) / 2
    new_fy = (fy + middle_y) / 2
    new_fx = (fx + middle_x) / 2
    for i in range(Y):  # for every row:
        for j in range(X):  # for every column
            rand = uniform(ab * 0.4, ab * 0.6)
            if on_ellipse(rand, new_ey, new_ex, new_fy, new_fx, i, j):
                dist = int(distance(middle_y, middle_x, i, j))
                uni_array[i][j] = - (dist * 503)


def create_galaxy(size, galaxies_number = 1):
    galaxies = []
    for i in range(galaxies_number):
        # create two random focal points
        ex = randint(0, X - 1)
        ey = randint(0, Y - 1)
        rand = randint(size, 2 * size)
        fx = ex + rand
        rand = randint(-size, size)
        fy = ey + rand
        rand = uniform(1.1, 1.3)
        ab = distance(ey, ex, fy, fx) * rand
        galaxies.append((ab, ey, ex, fy, fx))
    for i in range(Y):  # for every row:
        for j in range(X):  # for every column
            for t in galaxies:
                ab = t[0]
                rand = uniform(ab * (7 / 8), ab * (9 / 8))
                if on_ellipse(rand, t[1], t[2], t[3], t[4], i, j) and uni_array[i][j] >= 0:
                    uni_array[i][j] = 0
    for t in galaxies:
        enlarge_galaxy(t[0], t[1], t[2], t[3], t[4], )


def distance(y1, x1, y2, x2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    return dist


def set_random_points(probability):
    # put value of 1 on random positions in an array
    for i in range(Y):  # for every row:
        for j in range(X):  # for every column
            rand = randint(0, probability)
            if rand == 0:
                uni_array[i][j] = 1


def draw_image():
    for i in range(Y):  # for every row:
        for j in range(X):  # for every column
            if uni_array[i][j] == 1:  # color the pixel if there is a value in array
                rand = randint(0, 1)
                if rand == 0:
                    pixels[j, i] = (0, 0, 255)
                else:
                    pixels[j, i] = (0, 255, 255)
            elif uni_array[i][j] == 0:
                pixels[j, i] = (0, 0, 0)
            elif uni_array[i][j] % 503 == 0:
                num = uni_array[i][j] // 503
                rand = uniform(2.5, 3.5)
                pixels[j, i] = (int(255 + rand * num), 0, 255)
            elif uni_array[i][j] < 0:
                pixels[j, i] = (255, 255 + uni_array[i][j], 255 + 7 * uni_array[i][j])
            else:
                pass


#  create an array to represent matter in universe
RESOLUTION = (1080, 720)
X = RESOLUTION[0]
Y = RESOLUTION[1]

uni_array = [[0 for i in range(X)] for j in range(Y)]
uni_array = np.array(uni_array)
background = Image.new('RGB', RESOLUTION, "black")  # create a new black image
pixels = background.load()

set_random_points(20)
create_stars(20)
create_stars(70)
create_stars(150)
create_galaxy(50)
create_galaxy(80)
create_galaxy(170)
draw_image()
background.show()
for i in range(100):
    rand = randint(3, 10)
    create_stars(rand)
draw_image()
background.show()
background.save("uni" + str(6) + ".png")
