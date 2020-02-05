from random import randint

random_number = '0'


def make_number():
    global random_number
    random_number_tmp = []
    while len(random_number_tmp) < 4:
        x = (str(randint(1, 9)) if len(random_number_tmp) == 0 else str(randint(0, 9)))
        if x not in random_number_tmp:
            random_number_tmp.append(x)
    random_number = ''.join(random_number_tmp)
    print(random_number)


def check_the_number(user_number):
    animals = {'bulls': 0, 'cows': 0}
    for i in range(0, len(random_number)):
        if user_number[i] == random_number[i]:
            animals['bulls'] += 1
        elif user_number[i] in random_number:
            animals['cows'] += 1
    return animals
