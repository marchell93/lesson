# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import os
import zipfile


class StatisticChar:

    def __init__(self, file_name):
        self.file_name = file_name
        self.work_stat = {}
        self.report_stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.work_stat:
                    self.work_stat[char] += 1
                else:
                    self.work_stat[char] = 1

    def sorting_method(self):
        pass

    def write_on_console(self):
        count = 0
        format_chars = ['+', '-', 'буква', 'частота', 'итого']
        head_line = f'{format_chars[0]:-<11}{format_chars[0]:-<11}{format_chars[0]}'
        words_line = f'|{format_chars[2]:^10}|{format_chars[3]:^10}|'
        print(head_line)
        print(words_line)
        print(head_line)
        for key, value in self.report_stat.items():
            count += int(value)
            line = f'|{key:^10}|{value:^10}|'
            print(line)
        print(head_line)
        count_line = f'|{format_chars[4]:^10}|{str(count):^10}|'
        print(count_line)
        print(head_line)


class StatisticCharFreqDecrease(StatisticChar):

    def sorting_method(self):
        sorted_stat = sorted(self.work_stat.items(), key=lambda pair: pair[1], reverse=True)
        self.report_stat = dict(sorted_stat)


class StatisticCharFreqIncrease(StatisticChar):

    def sorting_method(self):
        sorted_stat = sorted(self.work_stat.items(), key=lambda pair: pair[1], reverse=False)
        self.report_stat = dict(sorted_stat)


class StatisticCharAlpIncrease(StatisticChar):

    def sorting_method(self):
        sorted_stat = sorted(self.work_stat.items(), key=lambda pair: pair[0], reverse=False)
        self.report_stat = dict(sorted_stat)


class StatisticCharAlpDecrease(StatisticChar):

    def sorting_method(self):
        sorted_stat = sorted(self.work_stat.items(), key=lambda pair: pair[0], reverse=True)
        self.report_stat = dict(sorted_stat)


if __name__ == '__main__':
    input_path = os.path.join(f'{os.path.curdir}', f'python_snippets\\voyna-i-mir.txt.zip')
    choice_class = {
        1: {'static_class': StatisticCharFreqDecrease, 'title': 'Вы выбрали сортировку по частоте по убыванию'},
        2: {'static_class': StatisticCharFreqIncrease, 'title': 'Вы выбрали сортировку по частоте по возрастанию'},
        3: {'static_class': StatisticCharAlpIncrease, 'title': 'Вы выбрали сортировку по алфавиту по возрастанию'},
        4: {'static_class': StatisticCharAlpDecrease, 'title': 'Вы выбрали сортировку по алфавиту по убыванию'},
    }
    while True:
        flag_char = int(input('Если Вы желаете упорядочить буквенные символы произведения Войны и мир по частоте по '
                              'убыванию нажмите 1\nЕсли Вы желаете упорядочить буквенные символы произведения Войны и '
                              'мир по частоте по возрастанию нажмите 2\nЕсли Вы желаете упорядочить буквенные символы '
                              'произведения Войны и мир по алфавиту по возрастанию нажмите 3\nЕсли Вы желаете '
                              'упорядочить буквенные символы произведения Войны и мир по алфавиту по убыванию нажмите '
                              '4\n'))

        if flag_char in choice_class:
            print(choice_class[flag_char]['title'])
            stat = choice_class[flag_char]['static_class'](input_path)
            stat.collect()
            stat.sorting_method()
            stat.write_on_console()
            break
        else:
            print(f'Вы ввели неверное число "{flag_char}", попробуйте еще раз!!!')


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

# зачет!