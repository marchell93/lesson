# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __init__(self):
        self.obj = 'Вода'

    def __str__(self):
        return f'{self.obj}'

    def __add__(self, other):
        if other.obj == 'Воздух':
            return Storm()
        elif other.obj == 'Огонь':
            return Vapor()
        elif other.obj == 'Земля':
            return Dirt()
        else:
            return None


class Air:

    def __init__(self):
        self.obj = 'Воздух'

    def __str__(self):
        return f'{self.obj}'

    def __add__(self, other):
        if other.obj == 'Огонь':
            return Thunderbolt()
        elif other.obj == 'Земля':
            return Dust()
        elif other.obj == 'Вода':
            return Storm()
        else:
            return None


class Fire:

    def __init__(self):
        self.obj = 'Огонь'

    def __str__(self):
        return f'{self.obj}'

    def __add__(self, other):
        if other.obj == 'Земля':
            return Lava()
        elif other.obj == 'Вода':
            return Vapor()
        elif other.obj == 'Воздух':
            return Thunderbolt()
        else:
            return None


class Ground:

    def __init__(self):
        self.obj = 'Земля'

    def __str__(self):
        return f'{self.obj}'

    def __add__(self, other):
        if other.obj == 'Вода':
            return Dirt()
        elif other.obj == 'Огонь':
            return Lava()
        else:
            return None


class Storm:

    def __init__(self):
        self.obj = 'Шторм'

    def __str__(self):
        return f'{self.obj}'


class Vapor:

    def __init__(self):
        self.obj = 'Пар'

    def __str__(self):
        return f'{self.obj}'


class Dirt:

    def __init__(self):
        self.obj = 'Грязь'

    def __str__(self):
        return f'{self.obj}'


class Thunderbolt:

    def __init__(self):
        self.obj = 'Молния'

    def __str__(self):
        return f'{self.obj}'


class Dust:

    def __init__(self):
        self.obj = 'Пыль'

    def __str__(self):
        return f'{self.obj}'


class Lava:

    def __init__(self):
        self.obj = 'Лава'

    def __str__(self):
        return f'{self.obj}'


print(f'{Water()} + {Air()} = {Water() + Air()}')
print(f'{Water()} + {Fire()} = {Water() + Fire()}')
print(f'{Water()} + {Ground()} = {Water() + Ground()}')
print(f'{Air()} + {Fire()} = {Air() + Fire()}')
print(f'{Air()} + {Ground()} = {Air() + Ground()}')
print(f'{Fire()} + {Ground()} = {Fire() + Ground()}')

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
