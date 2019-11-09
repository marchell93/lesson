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


def full_shapes(point, angle, length, number_of_sides, color):
    # Заносим точку начала рисования фугуры в переменную point_0, чтобы в дальнейшем использовать в sd.line()
    point_0 = point
    angle_delta = 360 / number_of_sides
    for i in range(number_of_sides - 1):
        v = sd.get_vector(point, angle, length)
        v.draw(color=color)
        point = v.end_point
        angle = angle + angle_delta
    sd.line(start_point=point, end_point=point_0, color=color)


def triangle_modification(point, angle, length, color):
    number_of_sides = 3
    full_shapes(point, angle, length, number_of_sides, color)


def square_modification(point, angle, length, color):
    number_of_sides = 4
    full_shapes(point, angle, length, number_of_sides, color)


def hexagon_modification(point, angle, length, color):
    number_of_sides = 6
    full_shapes(point, angle, length, number_of_sides, color)


def pentagon_modification(point, angle, length, color):
    number_of_sides = 5
    full_shapes(point, angle, length, number_of_sides, color)


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
        triangle_modification(point_triangle, angle, length, color_figure)
        square_modification(point_square, angle, length, color_figure)
        hexagon_modification(point_hexagon, angle, length, color_figure)
        pentagon_modification(point_pentagon, angle, length, color_figure)
        break
    else:
        print('Вы ввели некоректный номер!')
sd.pause()

# зачет!
