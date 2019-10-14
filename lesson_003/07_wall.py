# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# Счётчик для циклов
count = 1
# Цикл считающий координату y
for y in range(0, 600, 50):
    # Условие необходимое для определения какой ряд кирпичей мы кладем
    if count % 2 != 0:
        x_range = -50
    else:
        x_range = 0
    for x in range(x_range, 600, 100):
        point_start_first = sd.get_point(x, y)
        point_finish_first = sd.get_point(x + 100, y + 50)
        sd.rectangle(point_start_first, point_finish_first, width=3)
    count += 1
sd.pause()
