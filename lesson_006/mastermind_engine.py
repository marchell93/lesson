from random import randint

_random_number = 0


def make_number():
    global _random_number
    _random_number = randint(1000, 9999)
    print(_random_number)
    return str(_random_number)


def check_the_number(_hidden_number, _user_number):
    animals = {'bulls': 0, 'cows': 0}
    for i in range(0, len(_hidden_number)):
        if _user_number[i] == _hidden_number[i]:
            animals['bulls'] += 1
        elif _user_number[i] in _hidden_number:
            animals['cows'] += 1
        else:
            pass
    return animals
