# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


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


print(f'Возможные фигуры:\n\t0 : треугольник\n\t1 : квадрат\n\t2 : пятиугольник\n\t3 : шестиугольник\n\t')
angle = 10
length = 100
color = sd.COLOR_DARK_ORANGE
start_point = sd.get_point(250, 250)
while True:
    user_number = int(input('Введите желаемую фигуру: '))
    if user_number == 0:
        triangle(start_point, angle, length, color)
        break
    elif user_number == 1:
        square(start_point, angle, length, color)
        break
    elif user_number == 2:
        pentagon(start_point, angle, length, color)
        break
    elif user_number == 3:
        hexagon(start_point, angle, length, color)
        break
    else:
        print('Вы ввели некоректный номер!')
sd.pause()
