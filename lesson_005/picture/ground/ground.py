import simple_draw as sd


def land():
    point_start = sd.get_point(0, 0)
    point_finish = sd.get_point(1200, 50)
    sd.rectangle(point_start, point_finish, color=sd.COLOR_DARK_YELLOW, width=0)
