# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1, room_2


def room_residents(residents):
    for resident in residents.folks:
        print(f"В комнате {residents.__name__} живет: {resident}")


room_residents(room_1)
room_residents(room_2)

# зачет!
