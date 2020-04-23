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

    def __init__(self, pathfile, filename):
        # Спасибо большое за замечание, но мне кажется, что конкретно в данном случае лучше сделать именно так,
        # потому что, переменную self.filename я далее использую по коду
        self.filepath = os.path.join(pathfile, filename)
        self.filename = filename

    def run(self):
        ticker = self.filename.strip('.csv')

        volatility = 0.0
        min_price, max_price = self.open_file()
        if max_price and min_price:
            average_price = (max_price + min_price) / 2
            volatility = ((max_price - min_price) / average_price) * 100

        return ticker, volatility

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
    print(f'Нулевая волатильность:\n{konv_to_str}')


def print_total_volatility(total_volatility):
    count = 0
    len_tot_vol = len(total_volatility)
    print(f'Максимальная волатильность:')
    for key, value in total_volatility.items():
        count += 1
        if 3 >= count >= 1:
            print(f'{key} - {round(value, 3)} %')
        elif count == 4:
            print(f'Минимальная волатильность:')
        elif len_tot_vol - 2 <= count <= len_tot_vol:
            print(f'{key} - {round(value, 3)} %')


global_total_volatility = {}
global_null_volatility = []

if __name__ == '__main__':
    for dir, subdir, filenames in os.walk(r'trades'):
        volatilitys = [Volatility(dir, filename) for filename in filenames]
        for vol in volatilitys:
            ticker, volatility = vol.run()
            if volatility == 0.0:
                global_null_volatility.append(ticker)
            else:
                global_total_volatility[ticker] = volatility
    global_total_volatility = dict(sorted(global_total_volatility.items(), key=lambda pair: pair[1], reverse=True))
    print_total_volatility(global_total_volatility)
    print_null_volatility(global_null_volatility)
# зачет!
