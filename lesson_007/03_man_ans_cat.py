# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def pick_up_cat(self, cat):
        self.cat = cat
        self.cat.house = self.house
        cprint(f'{self.name} подобрал кота на улице и принес его домой', color='cyan')

    def shopping_cat_eat(self):
        if self.house.money >= 50:
            self.house.food_for_cat += 50
            self.house.money -= 50
            cprint('{} сходил в магазин за кошачьей едой'.format(self.name), color='magenta')
        else:
            cprint('Денег нет, голодай кот!', color='magenta')

    def clear_house(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint(f'{self.name} убрал дом, готов к новым делам', color='magenta')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.house.food < 10:
            self.shopping()
        elif self.fullness < 25:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif self.house.food_for_cat <= 10:
            self.shopping_cat_eat()
        elif self.house.dirt >= 100 and self.fullness >= 20:
            self.clear_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.food_for_cat = 0
        self.dirt = 0

    def __str__(self):
        return f'В доме человеческой еды осталось {self.food}, кошачей еды осталось {self.food_for_cat}, ' \
               f'денег осталось {self.money}, дом грязный на {self.dirt} баллов'


class Cat:

    def __init__(self, name):
        self.fullness = 50
        self.house = None
        self.name = name

    def __str__(self):
        return f'Сытость кота {self.name}а составляет {self.fullness}'

    def sleep(self):
        self.fullness -= 10
        cprint(f'Котик {self.name} поспал!', color='blue')

    def eat(self):
        if self.house.food_for_cat >= 10:
            self.fullness += 20
            self.house.food_for_cat -= 10
            cprint(f'Котик {self.name} наелся!', color='green')
        else:
            cprint(f'Нет еды для кота {self.name}', color='red')

    def tear_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint(f'Котик {self.name} подрал обои, хозяин убирай)))!', color='grey')

    def act(self):
        if self.fullness < 0:
            cprint(f'Котик {self.name} умер...', color='red')
            return
        dice = randint(1, 2)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.tear_wallpaper()


# Максимальное количество котов, которое может прокормить человек = 5...если больше, то кто нибудь останется голодным
cats = [
    Cat(name='Юджин'),
    Cat(name='Бон'),
    Cat(name='Черныш'),
    Cat(name='Барсик'),
    Cat(name='Чубайс'),
    # Cat(name='Тузик'),
]

citizen = Man(name='Марк')
my_sweet_home = House()
# my_cat = Cat(name='Юджин')
citizen.go_to_the_house(house=my_sweet_home)
for cat in cats:
    citizen.pick_up_cat(cat=cat)
# citizen.pick_up_cat(cat=my_cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    citizen.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    print(citizen)
    for cat in cats:
        print(cat)
    # print(my_cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

# зачет!
