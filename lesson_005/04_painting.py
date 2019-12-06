# -*- coding: utf-8 -*-
import simple_draw as sd
from picture.ground.ground import land
from picture.sky.snow import snowfall
from picture.ground.house import wall
from picture.ground.house import roof
from picture.ground.house import window
from picture.ground.house import smile
from picture.sky.sun import sun
from picture.ground.tree import tree
from picture.sky.rainbow import rainbow
from picture.sky.cloud import cloud

sd.resolution = (1200, 600)
# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# Переменные для функции tree()
start_point = sd.get_point(950, 30)
angle = 90
length = 80
delta = 30
# Рисуем картину
land()
wall()
roof()
window()
smile()
sun()
tree(start_point, angle, length, delta)
rainbow()
cloud()
snowfall()
sd.sleep(0.1)

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
sd.pause()

# Отлично получилось!
# зачет!
