# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):

    def shape(point, angle, length):
        point_0 = point
        angle_delta = 360 / n
        for i in range(n - 1):
            v = sd.get_vector(point, angle, length)
            v.draw()
            point = v.end_point
            angle = angle + angle_delta
        sd.line(start_point=point, end_point=point_0)

    return shape


draw_shapes = get_polygon(n=5)
draw_shapes(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()

# зачет!
