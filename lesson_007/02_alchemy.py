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
        self.element = 'Вода'

    def __str__(self):
        return f'{self.element}'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Ground):
            return Dirt()
        else:
            return None


class Air:

    def __init__(self):
        self.element = 'Воздух'

    def __str__(self):
        return f'{self.element}'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Thunderbolt()
        elif isinstance(other, Ground):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        else:
            return None


class Fire:

    def __init__(self):
        self.element = 'Огонь'

    def __str__(self):
        return f'{self.element}'

    def __add__(self, other):
        if isinstance(other, Ground):
            return Lava()
        elif isinstance(other, Water):
            return Vapor()
        elif isinstance(other, Air):
            return Thunderbolt()
        else:
            return None


class Ground:

    def __init__(self):
        self.element = 'Земля'

    def __str__(self):
        return f'{self.element}'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm:

    def __init__(self):
        self.element = 'Шторм'

    def __str__(self):
        return f'{self.element}'


class Vapor:

    def __init__(self):
        self.element = 'Пар'

    def __str__(self):
        return f'{self.element}'


class Dirt:

    def __init__(self):
        self.element = 'Грязь'

    def __str__(self):
        return f'{self.element}'


class Thunderbolt:

    def __init__(self):
        self.element = 'Молния'

    def __str__(self):
        return f'{self.element}'


class Dust:

    def __init__(self):
        self.element = 'Пыль'

    def __str__(self):
        return f'{self.element}'


class Lava:

    def __init__(self):
        self.element = 'Лава'

    def __str__(self):
        return f'{self.element}'


print(f'{Water()} + {Air()} = {Water() + Air()}')
print(f'{Water()} + {Fire()} = {Water() + Fire()}')
print(f'{Water()} + {Ground()} = {Water() + Ground()}')
print(f'{Air()} + {Fire()} = {Air() + Fire()}')
print(f'{Air()} + {Ground()} = {Air() + Ground()}')
print(f'{Fire()} + {Ground()} = {Fire() + Ground()}')

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

# зачет!
