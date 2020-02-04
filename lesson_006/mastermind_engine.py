from random import randint

random_number = '0'
user_number = '0'


def make_number():
    global random_number
    random_number_tmp = []
    while len(random_number_tmp) < 4:
        x = (str(randint(1, 9)) if len(random_number_tmp) == 0 else str(randint(0, 9)))
        if x not in random_number_tmp:
            random_number_tmp.append(x)
    random_number = ''.join(random_number_tmp)
    print(random_number)


def input_and_verify_user_number():
    while True:
        global user_number
        user_number = input('Введите Ваше число: ')
        if not user_number.isdigit():
            print('Вы ввели неверные символы, вводите только цифры!')
        elif user_number[0] == '0':
            print('Первое введеное число равно нулю, такого быть не должно, введите число, '
                  'которое начинается с другой цифры!')
        elif len(user_number) != 4:
            print('Вы ввели неверное количество символов, введите 4 цифры!')
        elif len(set(user_number)) != 4:
            print('Вы ввели повторяющиеся числа, введите заново значение с неповторяющимися цифрами!')
        else:
            break


def check_the_number():
    animals = {'bulls': 0, 'cows': 0}
    for i in range(0, len(random_number)):
        if user_number[i] == random_number[i]:
            animals['bulls'] += 1
        elif user_number[i] in random_number:
            animals['cows'] += 1
    return animals


def get_random_number():
    """
        Функция для отображения загадонного числа при окончании игры
    """
    return random_number
