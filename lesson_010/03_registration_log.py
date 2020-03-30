# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


def write_log_file(line, name_file):
    with open(name_file, mode='a', encoding='utf-8') as file:
        file.write(line)


with open('registrations.txt', mode='r', encoding='utf-8') as input_file:
    for i, line in enumerate(input_file):
        try:
            name, email, age = line.split(' ')
            print(f'Имя: {name}, емаил: {email}, возраст: {age}')
        except ValueError as exc:
            yui = exc.args[0]
            if 'got 0' in exc.args[0]:
                line_conf = f'Не могу обработать пустую строку № {i}, {exc} в строке {line}\n'
                print(line_conf)
                write_log_file('registrations_bad.log', line_conf)
            else:
                line_conf = f'Не могу обработать строку № {i}, {exc} в строке {line}\n'
                print(line_conf)
                write_log_file('registrations_bad.log', line_conf)
                # print(exc)
