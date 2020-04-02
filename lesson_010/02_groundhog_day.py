# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint
from random import choice
from termcolor import cprint

ENLIGHTENMENT_CARMA_LEVEL = 777


class StrMainClass(Exception):

    def __init__(self):
        super().__init__()
        self.message = None

    def __str__(self):
        return self.message


class IamGoodError(StrMainClass):

    def __init__(self):
        super().__init__()
        self.message = 'Режим Бога включен!!!'


class DrunkError(StrMainClass):

    def __init__(self):
        super().__init__()
        self.message = 'Объект напился!!!'


class CarCrashError(StrMainClass):

    def __init__(self):
        super().__init__()
        self.message = 'Объект разбился на машине!!!'


class GluttonyError(StrMainClass):

    def __init__(self):
        super().__init__()
        self.message = 'Объект обожрался!!!'


class DepressionError(StrMainClass):

    def __init__(self):
        super().__init__()
        self.message = 'Объект в депресии!!!'


class SuicideError(StrMainClass):

    def __init__(self):
        super().__init__()
        self.message = 'Объект покончил жизнь самоубийством!!!'


def one_day(finish_carma):
    exceptions = [IamGoodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]
    carma = randint(1, 7)
    probability = randint(1, 13)
    if probability == 3:
        choice_exception = choice(exceptions)
        raise choice_exception
    else:
        finish_carma += carma
    return finish_carma


def write_to_log(line_exception):
    with open('log_exceptions.txt', mode='a', encoding='utf-8') as file:
        file.write(line_exception)


if __name__ == '__main__':
    day = 0
    full_carma = 0
    while full_carma < ENLIGHTENMENT_CARMA_LEVEL:
        try:
            day += 1
            cprint(f'================== День {day} ==================', color='red')
            full_carma = one_day(full_carma)
            cprint(f'Карма объекта: {full_carma} ед.', color='green')
        except StrMainClass as exc:
            line = f'Поймано исключение {exc} на {day} дне!!!\n'
            write_to_log(line)
            print(line)


# https://goo.gl/JnsDqu

# зачет!