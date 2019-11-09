# -*- coding: utf-8 -*-

import simple_draw as sd


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

x = []
y = []
length_of_snowflake = []

for _ in range(N):
    x.append(sd.random_number(0, 600))
    y.append(sd.random_number(300, 650))
    length_of_snowflake.append(sd.random_number(10, 50))
while True:
    sd.start_drawing()
    for i in range(N):
        point_0 = sd.get_point(x[i], y[i])
        sd.snowflake(center=point_0, length=length_of_snowflake[i], color=sd.background_color)
        y[i] -= 5
        if y[i] < length_of_snowflake[i]:
            y[i] = sd.random_number(600, 650)
            x[i] = sd.random_number(0, 600)
            sd.snowflake(center=point_0, length=length_of_snowflake[i], color=sd.COLOR_WHITE)
        x[i] += sd.random_number(-5, 5)
        point_1 = sd.get_point(x[i], y[i])
        sd.snowflake(center=point_1, length=length_of_snowflake[i], color=sd.COLOR_WHITE)
        sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# По данному заданию прошу помощи...
# Сделал как смог...
# Если убираю sd.clear_screen() отстаются следы на экране.
# Усложненное задание не делал, но очень хочу...
# Посмотрите пожайлуста код, укажите на мои недостатки.
# Заранее спасибо!!!

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

# зачет!


