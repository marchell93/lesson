# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import (create_snowflake, draw_snowflake_color, move_snowflake, count_snowflake_bottom_of_screen,
                      delete_snowflake, create_snowflake_modified
                      )

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

number_of_snowflake = 20
# создать_снежинки(N)

x, y, length_of_snowflake = create_snowflake(number_of_snowflake)
while True:
    sd.start_drawing()
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    draw_snowflake_color(number_of_snowflake, x, y, length_of_snowflake, sd.background_color)
    #  сдвинуть_снежинки()
    move_snowflake(number_of_snowflake, x, y)
    #  нарисовать_снежинки_цветом(color)
    draw_snowflake_color(number_of_snowflake, x, y, length_of_snowflake, sd.COLOR_WHITE)
    #  если есть номера_достигших_низа_экрана() то
    count_snowflake_bottom_of_scr = count_snowflake_bottom_of_screen(number_of_snowflake, y, length_of_snowflake)
    if count_snowflake_bottom_of_scr:
        # удалить_снежинки(номера)
        delete_snowflake(count_snowflake_bottom_of_scr, x, y, length_of_snowflake)
        # создать_снежинки(count)
        create_snowflake_modified(count_snowflake_bottom_of_scr, x, y)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# зачет!
