# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


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


shapes = {
    0: {'title': 'треугольник', 'function': triangle_modification},
    1: {'title': 'квадрат', 'function': square_modification},
    2: {'title': 'пятиугольник', 'function': pentagon_modification},
    3: {'title': 'шестиугольник', 'function': hexagon_modification}
}

print('Возможные фигуры:')
for number, shape in shapes.items():
    print(f"{number} : {shape['title']}")
angle = 10
length = 100
color = sd.COLOR_DARK_ORANGE
start_point = sd.get_point(250, 250)
while True:
    user_number = int(input('Введите желаемую фигуру: '))
    if user_number in shapes:
        function_name = shapes[user_number]['function']
        function_name(start_point, angle, length, color)
        break
    else:
        print('Вы ввели некоректный номер!')
sd.pause()

# зачет!
