# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

sd.resolution = (1200, 600)


def triangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length)
    v3.draw()


def square(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length)
    v4.draw()


def hexagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length)
    v5.draw()
    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length)
    v6.draw()


def pentagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 75, length=length)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 140, length=length)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 225, length=length)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 285, length=length)
    v5.draw()


# angle = 10
# length = 100
# point_triangle = sd.get_point(150, 150)
# triangle(point_triangle, angle, length)
# point_square = sd.get_point(600, 150)
# square(point_square, angle, length)
# point_hexagon = sd.get_point(600, 350)
# hexagon(point_hexagon, angle, length)
# point_pentagon = sd.get_point(150, 350)
# pentagon(point_pentagon, angle, length)

# Вторая часть задания ---------------------------------------------------------------------------------------------


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


angle = 10
length = 100
color = sd.COLOR_CYAN
point_triangle = sd.get_point(150, 150)
triangle_modification(point_triangle, angle, length, color)
point_square = sd.get_point(600, 150)
square_modification(point_square, angle, length, color)
point_hexagon = sd.get_point(600, 350)
hexagon_modification(point_hexagon, angle, length, color)
point_pentagon = sd.get_point(150, 350)
pentagon_modification(point_pentagon, angle, length, color)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()

# зачет!
