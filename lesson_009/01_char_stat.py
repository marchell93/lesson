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
    input_path = os.path.normpath('D:\Skillbox\Python - '
                              'разработчик с нуля\python_base\lesson_009\python_snippets/voyna-i-mir.txt.zip')
    stchar = StatisticChar(input_path)
    stchar.collect()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
