# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import argparse
from PIL import Image, ImageDraw, ImageFont


def make_ticket(fio, from_, to, date, save_to):
    im = Image.open('images/ticket_template.png')
    draw = ImageDraw.Draw(im)
    fnt = ImageFont.truetype(font='fonts/ofont.ru_Tengri.ttf', size=15)
    draw.text((45, 124), fio, font=fnt, fill='#000000')
    draw.text((45, 193), from_, font=fnt, fill='#000000')
    draw.text((45, 259), to, font=fnt, fill='#000000')
    draw.text((287, 259), date, font=fnt, fill='#000000')
    im.save(save_to)
    im.show()


parser = argparse.ArgumentParser()
parser.add_argument('--fio', type=str, help='ФИО пассажира', required=True, nargs=2)
parser.add_argument('--from_', type=str, help='Вылет', required=True)
parser.add_argument('--to', type=str, help='Прилет', required=True)
parser.add_argument('--date', type=str, help='Дата вылета', required=True)
parser.add_argument('--save_to', type=str, help='Путь куда сохранить билет', default='new_ticket.png')
args = parser.parse_args()

args.fio = ' '.join(args.fio)
make_ticket(args.fio, args.from_, args.to, args.date, args.save_to)
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
