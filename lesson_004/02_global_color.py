# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

sd.resolution = (1200, 600)


def triangle(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length)
    v3.draw(color=color)


def square(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length)
    v3.draw(color=color)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length)
    v4.draw(color=color)


def hexagon(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length)
    v3.draw(color=color)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length)
    v4.draw(color=color)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length)
    v5.draw(color=color)
    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length)
    v6.draw(color=color)


def pentagon(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 70, length=length)
    v2.draw(color=color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 150, length=length)
    v3.draw(color=color)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 210, length=length)
    v4.draw(color=color)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 293, length=length)
    v5.draw(color=color)


global_color = {
    0: {'title': 'red', 'value': sd.COLOR_RED},
    1: {'title': 'orange', 'value': sd.COLOR_ORANGE},
    2: {'title': 'yellow', 'value': sd.COLOR_YELLOW},
    3: {'title': 'green', 'value': sd.COLOR_GREEN},
    4: {'title': 'cyan', 'value': sd.COLOR_CYAN},
    5: {'title': 'blue', 'value': sd.COLOR_BLUE},
    6: {'title': 'purple', 'value': sd.COLOR_PURPLE}
    }

print('Возможные цвета:')
for number, color in global_color.items():
    print(f"{number} : {color['title']}")
angle = 10
length = 100
point_triangle = sd.get_point(150, 150)
point_square = sd.get_point(600, 150)
point_hexagon = sd.get_point(600, 350)
point_pentagon = sd.get_point(150, 350)
while True:
    user_number = int(input('Введите желаемый цвет: '))
    if user_number in global_color:
        color_figure = global_color[user_number]['value']
        triangle(point_triangle, angle, length, color_figure)
        square(point_square, angle, length, color_figure)
        hexagon(point_hexagon, angle, length, color_figure)
        pentagon(point_pentagon, angle, length, color_figure)
        break
    else:
        print('Вы ввели некоректный номер!')
sd.pause()
