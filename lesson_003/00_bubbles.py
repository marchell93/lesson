# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(500, 500)
radius = 10
for _ in range(3):
    radius += 5
    sd.circle(point, radius, width=2)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step, color):
    radius = 20
    for _ in range(3):
        radius += step
        sd.circle(point, radius, color=color)


point = sd.get_point(100, 100)
step = 10
color = sd.random_color()
bubble(point, step, color)

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    color = sd.random_color()
    bubble(point, 10, color)

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        color = sd.random_color()
        bubble(point, 10, color)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    step = random.randint(2, 15)
    bubble(point, step, color)

sd.pause()

# зачет!
