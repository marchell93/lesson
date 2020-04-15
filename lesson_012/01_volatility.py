# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>
import os


class Volatility:
    total_volatility = {}
    null_volatility = []

    def __init__(self, pathfile, filename):
        self.filepath = os.path.join(pathfile, filename)
        self.filename = filename

    def run(self):
        self.open_file()
        Volatility.total_volatility = dict(sorted(self.total_volatility.items(), key=lambda pair: pair[1], reverse=True))

    def open_file(self):
        total_price = []
        with open(self.filepath, mode='r', encoding='utf-8') as file:
            for line in file:
                data_from_file = line[:-1].split(',')
                try:
                    if float(data_from_file[2]):
                        total_price.append(float(data_from_file[2]))
                except ValueError:
                    print(f'Первая строка файла - заголовок... читаем дальше')
            self.calculation_volatility(total_price)

    def calculation_volatility(self, total_price):
        max_price = max(total_price)
        min_price = min(total_price)
        average_price = (max_price + min_price) / 2
        volatility = ((max_price - min_price) / average_price) * 100
        if volatility == 0.0:
            self.null_volatility.append(self.filename.strip('.csv'))
        else:
            self.total_volatility[self.filename.strip('.csv')] = volatility

    def print_null_volatility(self):
        konv_to_str = ', '.join(self.null_volatility)
        print(f'Нулевая волатильность:\n{konv_to_str}')

    def print_total_volatility(self):
        count = 0
        len_tot_vol = len(self.total_volatility)
        print(f'Максимальная волатильность:')
        for key, value in self.total_volatility.items():
            count += 1
            if 3 >= count >= 1:
                print(f'{key} - {round(value, 3)} %')
            elif count == 4:
                print(f'Минимальная волатильность:')
            elif len_tot_vol - 3 <= count <= len_tot_vol - 1:
                print(f'{key} - {round(value, 3)} %')


if __name__ == '__main__':
    for dir, subdir, filenames in os.walk('trades'):
        volatilitys = [Volatility(dir, filename) for filename in filenames]
        for vol in volatilitys:
            vol.run()
        vol.print_total_volatility()
        vol.print_null_volatility()
