# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#

import os
from threading import Thread, Lock


class Volatility(Thread):

    def __init__(self, pathfile, filename, total_volatility, null_volatility, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filepath = os.path.join(pathfile, filename)
        self.filename = filename
        self.total_volatility = total_volatility
        self.null_volatility = null_volatility
        self.global_lock = lock

    def run(self):
        min_price, max_price = self.open_file()

        if min_price and max_price:
            average_price = (max_price + min_price) / 2
            volatility = ((max_price - min_price) / average_price) * 100
            if volatility == 0.0:
                with self.global_lock:
                    self.null_volatility.append(self.filename.strip('.csv'))
            else:
                with self.global_lock:
                    self.total_volatility[self.filename.strip('.csv')] = volatility

    def open_file(self):
        max_price = None
        min_price = None
        with open(self.filepath, mode='r', encoding='utf-8') as file:
            for line in file:
                data_from_file = line[:-1].split(',')
                try:
                    price = float(data_from_file[2])
                    if not max_price or price > max_price:
                        max_price = price
                    if not min_price or price < min_price:
                        min_price = price
                except ValueError:
                    print(f'Первая строка файла - заголовок... читаем дальше')
        return min_price, max_price


def print_null_volatility(null_volatility):
    konv_to_str = ', '.join(null_volatility)
    print(f'Нулевая волатильность:\n\t{konv_to_str}')


def print_total_volatility(total_volatility):
    count = 0
    len_tot_vol = len(total_volatility)
    print(f'Максимальная волатильность:')
    for key, value in total_volatility.items():
        count += 1
        if 3 >= count >= 1:
            print(f'\t{key} - {round(value, 3)} %')
        elif count == 4:
            print(f'Минимальная волатильность:')
        elif len_tot_vol - 2 <= count <= len_tot_vol:
            print(f'\t{key} - {round(value, 3)} %')


global_total_volatility = {}
global_null_volatility = []
lock = Lock()
if __name__ == '__main__':
    for dir, subdir, filenames in os.walk('trades'):
        volatilitys = [Volatility(pathfile=dir, filename=filename, total_volatility=global_total_volatility,
                                  null_volatility=global_null_volatility, lock=lock) for filename in filenames]
        for vol in volatilitys:
            vol.start()
        for vol in volatilitys:
            vol.join()
        global_total_volatility = dict(sorted(global_total_volatility.items(), key=lambda pair: pair[1], reverse=True))
        print_total_volatility(global_total_volatility)
        print_null_volatility(global_null_volatility)
# зачет!
