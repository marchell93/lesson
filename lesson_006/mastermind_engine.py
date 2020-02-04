from random import randint

_random_number = '0'


def make_number():
    global _random_number
    random_number_tmp = []
    while len(random_number_tmp) < 4:
        x = str(randint(0, 9))  # TODO Нулем может быть только первое число, не не остальные
        if x not in random_number_tmp:
            random_number_tmp.append(x)
    _random_number = ''.join(random_number_tmp)
    print(_random_number)
    return _random_number  # TODO Возвращать не нужно, мы записали это значение в глобальную переменную


def check_the_number(_hidden_number, _user_number):
    animals = {'bulls': 0, 'cows': 0}
    for i in range(0, len(_hidden_number)):
        if _user_number[i] == _hidden_number[i]:
            animals['bulls'] += 1
        elif _user_number[i] in _hidden_number:
            animals['cows'] += 1
    return animals
