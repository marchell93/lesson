# -*- coding: utf-8 -*-

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

from random import randint
from termcolor import cprint


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return f"В доме осталось {self.money} денег, {self.food} человеческой еды, {self.cat_food} еды для котов, " \
               f"дом грязный на {self.dirt} процентов"


class Man:
    all_food = 0

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30
        self.happiness = 100
        self.quantity_food_consumed = 20

    def __str__(self):
        return f'У {self.name} сытость {self.fullness}, счастья {self.happiness}'

    def eat(self):
        if self.house.food >= self.quantity_food_consumed:
            self.fullness += self.quantity_food_consumed
            self.house.food -= self.quantity_food_consumed
            cprint(f'{self.name} покушал', 'magenta')
            Man.all_food += self.quantity_food_consumed
        else:
            cprint(f'В доме нет человеческой еды', 'red')

    def happy(self):
        if self.house.dirt > 90:
            self.happiness -= 10

    def pet_the_cat(self):
        self.happiness += 5
        cprint(f'{self.name} погладил/а кота', 'green')

    def death(self):
        if self.fullness <= 0:
            cprint(f'{self.name} умер от голода', 'red')
            return True
        elif self.happiness < 10:
            cprint(f'{self.name} умер от депресии', 'red')
            return True


class Husband(Man):
    all_money = 0

    def act(self):
        self.happy()
        dice = randint(1, 3)
        if self.fullness <= 10:
            self.eat()
        elif self.house.money < 100:
            self.work()
        elif self.happiness < 25:
            self.gaming()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.gaming()
        elif dice == 3:
            self.pet_the_cat()

    def work(self):
        self.house.money += 150
        self.fullness -= 10
        cprint(f'Муж сходил на работу!!!', 'green')
        Husband.all_money += 150

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        cprint(f'Муж поиграл в WoT!!!', 'grey')


class Wife(Man):
    all_fur_coat = 0

    def act(self):
        self.happy()
        dice = randint(1, 4)
        if self.house.food <= 20 and self.fullness >= 15:
            self.shopping()
        elif self.fullness <= 15:
            self.eat()
        elif self.house.dirt > 90 and self.fullness >= 10:
            self.clean_house()
        elif self.house.cat_food <= 10:
            self.shopping_cat_food()
        elif self.house.money > 400 and self.fullness >= 10:
            self.buy_fur_coat()
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.pet_the_cat()
        elif dice == 3:
            self.shopping_cat_food()
        elif dice == 4:
            self.shopping()

    def shopping(self):
        self.house.food += 100
        self.house.money -= 100
        self.fullness -= 10
        cprint('Жена сходила в магазин и купила еды!!!', 'yellow')

    def shopping_cat_food(self):
        self.house.cat_food += 10
        self.house.money -= 10
        self.fullness -= 10
        cprint(f'Жена сходила в магазин и купила для котов еды!!!', 'yellow')

    def buy_fur_coat(self):
        self.happiness += 60
        self.house.money -= 350
        self.fullness -= 10
        cprint('Жена купила шубу', 'red')
        Wife.all_fur_coat += 1

    def clean_house(self):
        self.house.dirt -= 90
        self.fullness -= 10
        cprint('Жена убралась в доме', 'red')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:
    all_cat_food = 0

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30

    def __str__(self):
        return f'У кота {self.name} сытость {self.fullness}'

    def act(self):
        dice = randint(1, 2)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.soil()

    def eat(self):
        if self.house.cat_food >= 10:
            self.fullness += 20
            self.house.cat_food -= 10
            cprint(f'Кот {self.name} покушал', 'yellow')
            Cat.all_cat_food += 10
        else:
            cprint(f'Для {self.name} нет еды в доме', 'red')

    def sleep(self):
        self.fullness -= 10
        cprint(f'Кот {self.name} поспал', 'green')

    def soil(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint(f'Кот {self.name} подрал обои', 'white')

    def death(self):
        if self.fullness <= 0:
            cprint(f'Кот {self.name} умер от голода', 'red')
            return True


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Man):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)
        self.quantity_food_consumed = 10

    def act(self):
        if self.fullness <= 15:
            self.eat()
        else:
            self.sleep()

    def sleep(self):
        self.fullness -= 5
        cprint(f'Малыш {self.name} поспал', 'white')


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
murzik = Cat(name='Мурзик', house=home)

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    if serge.death() or masha.death() or kolya.death() or murzik.death():
        break
    home.dirt += 5
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')
cprint('Отчёт за год:', 'yellow')
cprint(f'Заработано {Husband.all_money} денег', 'yellow')
cprint(f'Съедено {Man.all_food} человеческой еды', 'yellow')
cprint(f'Куплено {Wife.all_fur_coat} шуб', 'yellow')
cprint(f'Съедено котом {Cat.all_cat_food} еды', 'yellow')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

# зачет!
