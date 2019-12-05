import simple_draw as sd


def cloud():
    radius = 50
    color = sd.COLOR_BLUE
    for x in range(50, 201, 50):
        point_1 = sd.get_point(x, 550)
        point_2 = sd.get_point(x, 500)
        sd.circle(point_1, radius, width=0, color=color)
        sd.circle(point_2, radius, width=0, color=color)
