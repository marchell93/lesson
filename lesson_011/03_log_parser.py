# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
import time

event = 'NOK'
input_file = 'events.txt'


def main_events_collect(event_name, input_filename):
    print(f'Производится подсчет событий {event_name}\n')
    with open(input_filename, 'r', encoding='utf-8') as file:
        store_like_times = ''
        count = 1
        for line in file:
            if event_name in line:
                line = line.strip('[')
                line = line[:-5].strip(']')
                line = line.rsplit('.')
                times_data = time.strptime(line[0], '%Y-%m-%d %H:%M:%S')
                like_times = (f'{times_data[0]}-{times_data[1]:02d}-{times_data[2]:02d} ' +
                              f'{times_data[3]:02d}:{times_data[4]:02d}')
                if like_times in store_like_times:
                    count += 1
                else:
                    if store_like_times == '':
                        store_like_times = like_times
                    else:
                        yield store_like_times, count
                        store_like_times = like_times
                        count = 1


grouped_events = main_events_collect(event, input_file)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')

# зачет!
