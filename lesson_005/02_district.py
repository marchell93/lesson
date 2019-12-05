# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as cen_str_h1r1
from district.central_street.house1.room2 import folks as cen_str_h1r2
from district.central_street.house2.room1 import folks as cen_str_h2r1
from district.central_street.house2.room2 import folks as cen_str_h2r2
from district.soviet_street.house1.room1 import folks as sov_str_h1r1
from district.soviet_street.house1.room2 import folks as sov_str_h1r2
from district.soviet_street.house2.room1 import folks as sov_str_h2r1
from district.soviet_street.house2.room2 import folks as sov_str_h2r2

all_people = (cen_str_h1r1 + cen_str_h1r2 + cen_str_h2r1 + cen_str_h2r2 + sov_str_h1r1
              + sov_str_h1r2 + sov_str_h2r1 + sov_str_h2r2)
all_people_in_district_string = ', '.join(all_people)
print(f'На районе живут: {all_people_in_district_string}')

# зачет!
