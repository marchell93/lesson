# -*- coding: utf-8 -*-

import simple_draw as sd
from random import choice


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

list_x = []
# list_y = [650] * 20
list_length = []

for _ in range(N):
    list_x.append(sd.random_number(0, 600))
    list_length.append(sd.random_number(10, 100))
y = 650
while True:
    sd.clear_screen()
    sd.start_drawing()
    for i in range(N):
        point0 = sd.get_point(list_x[i], y)
        sd.snowflake(center=point0, length=list_length[i], color=sd.COLOR_WHITE)
        y -= 5
        if y < 0:
            break
        x = list_x[i] + 10
        point1 = sd.get_point(x, y)
        sd.snowflake(center=point0, length=list_length[i], color=sd.background_color)
        sd.snowflake(center=point1, length=list_length[i], color=sd.COLOR_WHITE)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


