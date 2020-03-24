# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import time


class ProcessingEvent:

    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.report_stat = {}

    def collect(self, event_name):
        print(f'Производится подсчет событий {event_name}\n')
        with open(self.input_filename, 'r', encoding='utf-8') as file:
            for line in file:
                if event_name in line:
                    line = line.strip('[')
                    line = line[:-5].strip(']')
                    line = line.rsplit('.')
                    self.convert_to_time(line=line[0])

    def convert_to_time(self, line):
        times_data = time.strptime(line, '%Y-%m-%d %H:%M:%S')
        self.pooling_of_data(times_data=times_data)

    def pooling_of_data(self, times_data):
        like_times = f'{times_data[0]}-{times_data[1]:02d}-{times_data[2]:02d} {times_data[3]:02d}:{times_data[4]:02d}'
        if like_times in self.report_stat:
            self.report_stat[like_times] += 1
        else:
            self.report_stat[like_times] = 1

    def write_to_file(self):
        with open(self.output_filename, 'a', encoding='utf-8') as file:
            for key, value in self.report_stat.items():
                line = f'[{key}] {value}\n'
                file.write(line)
                print(line)


class ProcessingEventHour(ProcessingEvent):

    def pooling_of_data(self, times_data):
        like_times = f'{times_data[0]}-{times_data[1]:02d}-{times_data[2]:02d} {times_data[3]:02d}'
        if like_times in self.report_stat:
            self.report_stat[like_times] += 1
        else:
            self.report_stat[like_times] = 1


class ProcessingEventMonth(ProcessingEvent):

    def pooling_of_data(self, times_data):
        like_times = f'{times_data[0]}-{times_data[1]:02d}'
        if like_times in self.report_stat:
            self.report_stat[like_times] += 1
        else:
            self.report_stat[like_times] = 1


class ProcessingEventYear(ProcessingEvent):

    def pooling_of_data(self, times_data):
        like_times = f'{times_data[0]}'
        if like_times in self.report_stat:
            self.report_stat[like_times] += 1
        else:
            self.report_stat[like_times] = 1


if __name__ == '__main__':
    static_class = None
    while static_class is None:
        flag_char = int(input('Если Вы желаете сгруппировать за каждую минуту события из Лог-файла нажмите 1\n'
                              'Если Вы желаете сгруппировать за каждый час события из Лог-файла нажмите 2\n'
                              'Если Вы желаете сгруппировать по месяцам события из Лог-файла нажмите 3\n'
                              'Если Вы желаете сгруппировать по годам события из Лог-файла нажмите 4\n'))
        if flag_char == 1:
            static_class = ProcessingEvent
            print('Вы выбрали группировку данных за каждую минуту')
        elif flag_char == 2:
            static_class = ProcessingEventHour
            print('Вы выбрали группировку данных за каждый час')
        elif flag_char == 3:
            static_class = ProcessingEventMonth
            print('Вы выбрали группировку данных по месяцам')
        elif flag_char == 4:
            static_class = ProcessingEventYear
            print('Вы выбрали группировку данных по годам')
        else:
            print(f'Вы ввели неверное число "{flag_char}", попробуйте еще раз!!!')
    stat = static_class('events.txt', 'new_events.txt')
    # Есть ньюанс при указании event_name...происходит совпадение последовательности букв в Лог-файле при описании
    # событий, таким образом, для более точного идентифицирования события перед командой " OK", в аргументе event_name,
    # я ставлю пробел, чтобы статистика событий с данной командой не попадала в статистику события "NOK"
    stat.collect('NOK')
    stat.write_to_file()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
