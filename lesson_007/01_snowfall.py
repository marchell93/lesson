# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(0, 600)
        self.y = sd.random_number(300, 650)
        self.length = sd.random_number(10, 50)
        self.point = None

    def move(self):
        self.y -= 5
        self.x += sd.random_number(-5, 5)
        self.point = sd.get_point(self.x, self.y)

    def draw(self):
        sd.snowflake(center=self.point, length=self.length, color=sd.COLOR_WHITE)

    def clear_previous_picture(self):
        if self.point is not None:
            sd.snowflake(center=self.point, length=self.length, color=sd.background_color)

    def can_fall(self):
        return self.y > self.length


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


# ---------------------------------------------------------------------------------------------------------------------
# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
def get_flakes(count):
    list_flakes = []
    for _ in range(count):
        new_flake = Snowflake()
        list_flakes.append(new_flake)
    return list_flakes


def get_fallen_flakes():
    fallen_flakes_count = 0
    for i, existing_flake in enumerate(flakes):
        if not existing_flake.can_fall():
            fallen_flakes_count += 1
            existing_flake.clear_previous_picture()
            del flakes[i]
    return fallen_flakes_count


def append_flakes(count_fallen_flakes):
    for _ in range(count_fallen_flakes):
        new_append_flake = Snowflake()
        flakes.append(new_append_flake)


flakes = get_flakes(20)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# зачет!
