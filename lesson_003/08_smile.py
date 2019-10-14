# -*- coding: utf-8 -*-

# (определение функций)
import random
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color):
    # Прорисовываем овал лица...точнее круг)))
    point = sd.get_point(x, y)
    radius = 50
    sd.circle(point, radius, color, 4)
    # Прорисовываем правый глаз смайлика
    point_right_eyes = sd.get_point(x + 15, y + 15)
    radius_right_eyes = radius - 45
    sd.circle(point_right_eyes, radius_right_eyes, color)
    # Прорисовываем левый глаз смайлика
    point_left_eyes = sd.get_point(x - 15, y + 15)
    radius_left_eyes = radius - 45
    sd.circle(point_left_eyes, radius_left_eyes, color)
    # Прорисовываем рот смайлика
    point_mouth_first = sd.get_point(x - 30, y - 5)
    point_mouth_second = sd.get_point(x - 15, y - 20)
    point_mouth_third = sd.get_point(x + 15, y - 20)
    point_mouth_fourth = sd.get_point(x + 30, y - 5)
    point_list = []
    point_list.extend([point_mouth_first, point_mouth_second, point_mouth_third, point_mouth_fourth])
    sd.lines(point_list, closed=False, color=color)


for _ in range(10):
    x = random.randint(50, 500)
    y = random.randint(50, 500)
    color = sd.random_color()
    smile(x, y, color)
sd.pause()

# зачет!
