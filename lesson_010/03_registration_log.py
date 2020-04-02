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


class NotNameError(Exception):

    def __init__(self, message, input_data=None):
        super().__init__(message, input_data)
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return f'("{self.message}", "{self.input_data}")'


class NotEmailError(Exception):

    def __init__(self, message, input_data=None):
        super().__init__(message, input_data)
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return f'("{self.message}", "{self.input_data}")'


class ControlValidationLine:

    def __init__(self, input_line):
        self.input_line = input_line

    def validation_line(self):
        count_arguments = self.input_line.split(' ')
        if len(count_arguments) == 3:
            name, email, age = count_arguments
            if age.isdigit():
                age = int(age)
            else:
                raise ValueError('Пользователь ввел данные в случайном порядке', self.input_line)
        else:
            raise ValueError('В строке нехватает элементов', self.input_line)
        if not name.isalpha():
            raise NotNameError('Поле имени содержит НЕ только буквы', input_data=self.input_line)
        elif '@' not in email or '.' not in email:
            raise NotEmailError('Поле емейл НЕ содержит @ или .(точку)', input_data=self.input_line)
        elif age < 10 or age > 99:
            raise ValueError('Поле возраст НЕ является числом от 10 до 99', self.input_line)


def write_to_log(line, output_file_name):
    with open(output_file_name, mode='a', encoding='utf-8') as output_file:
        output_file.write(line+'\n')


def condition_except(exc, count_line, output_file_name):
    excepts = f'Поймано моё исключение {exc} в строке {count_line}'
    print(excepts)
    write_to_log(excepts, output_file_name)


if __name__ == '__main__':
    with open('registrations.txt', mode='r', encoding='utf-8') as input_file:
        for i, line in enumerate(input_file):
            line = line[:-1]
            validation_line = ControlValidationLine(line)
            try:
                validation_line.validation_line()
                write_to_log(line, 'registrations_good.log')
            except ValueError as exc:
                condition_except(exc, i, 'registrations_bad.log')
            except NotNameError as exc_nne:
                condition_except(exc_nne, i, 'registrations_bad.log')
            except NotEmailError as exc_nee:
                condition_except(exc_nee, i, 'registrations_bad.log')

# зачет!
