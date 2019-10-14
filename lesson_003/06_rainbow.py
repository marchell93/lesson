# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x_start = 50
x_finish = 350
for color in rainbow_colors:
    point_start = sd.get_point(x_start, 50)
    point_finish = sd.get_point(x_finish, 450)
    sd.line(point_start, point_finish, color, width=4)
    x_start += 5
    x_finish += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
x_point = 500
y_point = -300
radius = 800
for color in rainbow_colors:
    point_start = sd.get_point(x_point, y_point)
    radius += 10
    sd.circle(point_start, radius, color, 10)
sd.pause()

# зачет!
