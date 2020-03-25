# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class FilesArrange:

    def __init__(self, input_path, output_path):
        self.input_path = os.path.normpath(input_path)
        self.output_path = os.path.normpath(output_path)
        self.full_file_path = None
        self.full_output_path = None

    def process(self):
        for dirpath, dirnames, filenames in os.walk(self.input_path):
            for file in filenames:
                self.get_time_files(dirpath, file)
                self.create_date_dirs()
                self.copy_files_to_date_dirs()

    def get_time_files(self, dirpath, file):
        self.full_file_path = os.path.join(dirpath, file)
        secs_create_file = os.path.getmtime(self.full_file_path)
        file_time = time.gmtime(secs_create_file)
        self.full_output_path = os.path.join(self.output_path, f'{file_time[0]}\\{file_time[1]:02d}')

    def create_date_dirs(self):
        if not os.path.exists(self.full_output_path):
            os.makedirs(self.full_output_path)
            print(f'Создали директорию {self.full_output_path}')

    def copy_files_to_date_dirs(self):
        shutil.copy2(self.full_file_path, self.full_output_path)
        print(f'Скорировали файл {self.full_file_path} в директорию {self.full_output_path}')


in_path = os.path.join(os.path.curdir, 'icons')
out_path = os.path.join(os.path.curdir, 'icons_by_year')
fa = FilesArrange(in_path, out_path)
fa.process()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

# зачет!
