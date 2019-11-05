# -*- coding: utf-8 -*-

import simple_draw as sd
import random
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

sd.resolution = (1200, 600)


def draw_branches(start_point, angle, length, delta):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    v1.draw(width=1)
    next_point = v1.end_point
    next_length = length * .75
    next_angle_left = angle - delta
    next_angle_right = angle + delta
    draw_branches(start_point=next_point, angle=next_angle_left, length=next_length, delta=delta)
    draw_branches(start_point=next_point, angle=next_angle_right, length=next_length, delta=delta)


root_point = sd.get_point(300, 30)
root_angle = 90
root_length = 100
delta = 30
draw_branches(start_point=root_point, angle=root_angle, length=root_length, delta=delta)
# -------------------------------------------------------------------------------------------------------------------

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg


def draw_branches_modification(start_point, angle, length):
    if length < 4:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    v1.draw(width=1)
    delta_angle = sd.random_number(18, 42)
    delta_length = random.uniform(.5, 1)
    next_point = v1.end_point
    next_length = length * delta_length
    next_angle_left = angle - delta_angle
    draw_branches_modification(start_point=next_point, angle=next_angle_left, length=next_length)
    next_angle_right = angle + delta_angle
    draw_branches_modification(start_point=next_point, angle=next_angle_right, length=next_length)


root_point = sd.get_point(300, 30)
root_angle = 90
root_length = 100
draw_branches_modification(start_point=root_point, angle=root_angle, length=root_length)

# Пригодятся функции
# sd.random_number()

sd.pause()

# зачет!

